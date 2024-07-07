from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import cpu_count
from typing import Dict

import numpy as np
import pandas as pd
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
from umap import UMAP

from ..loaders.documents.base_document_loader import BaseDocumentLoader
from ..metrics.base_metric import BaseMetric
from ..samplers.clusters.hdsbcan_sampler import HDBSCANSampler


class MetricMapper:
    def __init__(
        self,
        document_loader: BaseDocumentLoader,
        transformer: SentenceTransformer,
        hdbscan_sampler: HDBSCANSampler,
        metrics: Dict[str, BaseMetric],
        runs: int = 1,
        umap_seed: int = None,
        out_dir: str = "default",
    ) -> None:
        self.document_loader = document_loader
        self.transformer = transformer
        self.hdbscan_sampler = hdbscan_sampler
        self.metrics = metrics
        self.runs = runs
        self.umap_seed = umap_seed
        self.out_dir = out_dir

    def cluster(self, hdbscan: HDBSCAN, embeddings: np.ndarray):
        clusters = hdbscan.fit_predict(embeddings)
        return clusters, embeddings

    def run(self):
        documents = self.document_loader.load_documents()

        embeddings = self.transformer.encode(
            documents, show_progress_bar=True, device="cpu"
        )

        sampler_names = [
            sampler.parameter_name
            for sampler in self.hdbscan_sampler.parameter_samplers
        ]

        metric_maps = {
            metric: pd.DataFrame(columns=sampler_names + [metric])
            for metric in self.metrics
        }

        progress_bar = tqdm(
            total=sum(1 for _ in self.hdbscan_sampler.iterate_configurations())
            * self.runs,
            desc=MetricMapper.__name__,
        )

        def compute_metrics(sampler_values, future):
            clusters, embeddings = future.result()
            for metric in self.metrics:
                metric_value = self.metrics[metric].perform_metric(
                    clusters=clusters, embeddings=embeddings
                )
                new_row = sampler_values + [metric_value]
                metric_maps[metric].loc[len(metric_maps[metric])] = new_row
            progress_bar.update(1)

        with ProcessPoolExecutor(max_workers=cpu_count()) as pool:
            for _ in range(self.runs):
                if self.umap_seed is not None:
                    random_state = self.umap_seed
                else:
                    random_state = np.random.randint(1, 2**32)

                reduced_embeddings = UMAP(
                    n_neighbors=15,
                    n_components=5,
                    min_dist=0.0,
                    metric="cosine",
                    random_state=random_state,
                ).fit_transform(embeddings)

                for hdbscan in self.hdbscan_sampler.iterate_configurations():
                    sampler_values = [
                        getattr(hdbscan, param_name) for param_name in sampler_names
                    ]
                    future_result = pool.submit(
                        self.cluster, hdbscan, reduced_embeddings
                    )
                    future_result.add_done_callback(
                        partial(compute_metrics, sampler_values)
                    )

        for metric, df in metric_maps.items():
            combined_df = df.groupby(sampler_names, as_index=False).agg(
                {metric: "mean"}
            )
            sorted_df = combined_df.sort_values(by=sampler_names)
            sorted_df.to_csv(f"{self.out_dir}/{metric}_map.csv", index=False)

        progress_bar.close()
        pool.shutdown(wait=True)
