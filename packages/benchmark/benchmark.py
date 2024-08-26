import os
import sys
import warnings
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from pathlib import Path

import torch

warnings.simplefilter(
    action="ignore",
    category=FutureWarning,
)
warnings.filterwarnings(
    "ignore", message="n_jobs value .* overridden to 1 by setting random_state.*"
)
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["KMP_WARNINGS"] = "false"
os.environ["OMP_DISPLAY_ENV"] = "FALSE"

import numpy as np
import polars as pl
import yaml
from clusview.loaders.documents.csv_concatenator import CSVConcatenator
from clusview.metrics.average_cluster_size import AverageClusterSize
from clusview.metrics.cluster_count import ClusterCount
from clusview.metrics.davies_bouldin_score import DaviesBouldinScore
from clusview.metrics.outlier_ratio import OutlierRatio
from clusview.metrics.silhouette_score import SilhouetteScore
from clusview.metrics.v_measure_score import VMeasureScore
from clusview.samplers.clusters.hdsbcan_sampler import HDBSCANSampler
from clusview.samplers.parameters.linear_sampler import LinearSampler
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from umap import UMAP

if len(sys.argv) < 2:
    print(
        "Please, provide the benchmark configuration YAML file path as a command-line argument."
    )
    sys.exit(1)


class DictAsMember(dict):
    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = DictAsMember(value)
        return value


benchmark = DictAsMember(
    yaml.safe_load(Path(sys.argv[1]).read_text()),
)

schema = {
    "dataset": pl.String,
    "model": pl.String,
    "umap_seed": pl.Int64,
    "min_cluster_size": pl.Int64,
    "min_samples": pl.Int64,
}

for metric in benchmark.metrics:
    schema[metric] = pl.Float64

df = pl.DataFrame(schema=schema)

datasets = benchmark.datasets
columns = benchmark.columns
models = benchmark.models
umap_seeds = benchmark.umap_seeds
min_cluster_size_range = range(
    benchmark.min_cluster_size.min, benchmark.min_cluster_size.max + 1
)
min_samples_range = range(benchmark.min_samples.min, benchmark.min_samples.max + 1)
metrics = {
    "SilhouetteScore": SilhouetteScore(),
    "DaviesBouldinScore": DaviesBouldinScore(),
    "OutlierRatio": OutlierRatio(),
    "ClusterCount": ClusterCount(),
    "AverageClusterSize": AverageClusterSize(),
}


def cluster(hdbscan: HDBSCAN, embeddings: np.ndarray, groundtruth: np.ndarray):
    clusters = hdbscan.fit_predict(embeddings)
    metrics["VMeasureScore"] = VMeasureScore(groundtruth_clusters=groundtruth, beta=1.0)
    metric_values = []
    for metric in metrics:
        metric_values.append(
            metrics[metric].perform_metric(clusters=clusters, embeddings=embeddings)
        )
    return metric_values, hdbscan.min_cluster_size, hdbscan.min_samples


if __name__ == "__main__":
    for dataset in datasets:
        documents = CSVConcatenator(dataset, columns).load_documents()
        groundtruth = np.where(
            pl.read_csv(dataset).select("status").to_series() == "Accepted", 1, 0
        )
        for model_name in models:
            print(f"Embedding {dataset} with {model_name}.")
            model = SentenceTransformer(model_name, trust_remote_code=True)
            embeddings = model.encode(documents, show_progress_bar=True, device="cpu")
            for umap_seed in umap_seeds:
                reduced_embeddings = UMAP(
                    n_neighbors=15,
                    n_components=5,
                    min_dist=0.0,
                    metric="cosine",
                    random_state=umap_seed,
                ).fit_transform(embeddings)
                hdbscan_sampler = HDBSCANSampler(
                    [
                        LinearSampler(
                            "min_cluster_size",
                            benchmark.min_cluster_size.min,
                            benchmark.min_cluster_size.max,
                            benchmark.min_cluster_size.max
                            - benchmark.min_cluster_size.min
                            + 1,
                        ),
                        LinearSampler(
                            "min_samples",
                            benchmark.min_samples.min,
                            benchmark.min_samples.max,
                            benchmark.min_samples.max - benchmark.min_samples.min + 1,
                        ),
                    ]
                )

                progress_bar = tqdm(
                    total=sum(1 for _ in hdbscan_sampler.iterate_configurations()),
                    desc=f"Clustering with UMAP seed {umap_seed}",
                )
                results = []

                with ProcessPoolExecutor(max_workers=cpu_count()) as pool:
                    for hdbscan in hdbscan_sampler.iterate_configurations():
                        future_result = pool.submit(
                            cluster, hdbscan, reduced_embeddings, groundtruth
                        )
                        future_result.add_done_callback(
                            lambda future: (
                                # df.extend(
                                #     pl.DataFrame(
                                #         [
                                #             [
                                #                 dataset,
                                #                 model_name,
                                #                 umap_seed,
                                #                 future.result()[1],
                                #                 future.result()[2],
                                #                 *future.result()[0],
                                #             ]
                                #         ],
                                #         schema=schema,
                                #         orient="row",
                                #     )
                                # ),
                                results.append(
                                    [
                                        dataset,
                                        model_name,
                                        umap_seed,
                                        future.result()[1],
                                        future.result()[2],
                                        *future.result()[0],
                                    ]
                                ),
                                progress_bar.update(1),
                            )
                        )

                df = df.extend(pl.DataFrame(results, schema=schema, orient="row"))
                pool.shutdown(wait=True)
                progress_bar.close()
            print()

    print("Ordering results.")
    df = df.sort(["dataset", "model", "umap_seed", "min_cluster_size", "min_samples"])
    print("Saving results to disk.")
    df.write_csv("./result/clusview.csv")
