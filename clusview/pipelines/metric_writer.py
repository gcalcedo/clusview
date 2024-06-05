import time
from concurrent import futures
from multiprocessing import cpu_count
from typing import Dict

import numpy as np
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer

from clusview.loaders import *
from clusview.loaders.documents.base_document_loader import BaseDocumentLoader
from clusview.metrics.base_metric import BaseMetric
from clusview.samplers.clusters.hdsbcan_sampler import HDBSCANSampler


class CVMetricWriter:
    """
    Clusview pipeline with these steps:
    - Load documents.
    - Embed documents and reduce dimensionality.
    - Iterate over HDSBCAN configuration samplings.
    - Compute metric maps.
    - Write maps to file system.
    """

    def __init__(
        self,
        document_loader: BaseDocumentLoader,
        transformer: SentenceTransformer,
        hdbscan_iterator: HDBSCANSampler,
        metrics: Dict[str, BaseMetric],
    ) -> None:
        self.document_loader = document_loader
        self.transformer = transformer
        self.metrics = metrics
        self.hdbscan_iterator = hdbscan_iterator

    def fit_bert(self, hdbscan, documents, embeddings, i, j):
        topic_model = BERTopic(hdbscan_model=hdbscan)
        topic_model.fit_transform(documents, embeddings)

        return topic_model, embeddings, i, j

    def run(self):
        documents = self.document_loader.load_documents()

        embeddings = self.transformer.encode(
            documents, show_progress_bar=True, device="cpu"
        )

        x_size = len(documents) + 1
        y_size = len(documents) + 1

        metric_maps = {}
        for metric in self.metrics:
            metric_maps[metric] = np.zeros((x_size, y_size), dtype=float)

        total_count = sum(1 for _ in self.hdbscan_iterator.iterate_configurations())
        count = 0
        start_time = time.time()

        def callback(future):
            nonlocal count
            nonlocal metric_maps
            nonlocal total_count
            nonlocal start_time
            count += 1
            elapsed_time = time.time() - start_time
            estimated_total_time = (elapsed_time / count) * total_count
            remaining_time = (estimated_total_time - elapsed_time) / 60
            print(f"[{count}/{total_count}] - {remaining_time:.2f} minutes left.")

            topic_model, embeddings, i, j = future.result()
            for metric in self.metrics:
                metric_maps[metric][i, j] = self.metrics[metric].perform_metric(
                    topic_model, embeddings
                )

        with futures.ProcessPoolExecutor(max_workers=cpu_count()) as pool:
            for hdbscan in self.hdbscan_iterator.iterate_configurations():
                param1_index = hdbscan.min_cluster_size
                param2_index = hdbscan.min_samples
                future_result = pool.submit(
                    self.fit_bert,
                    hdbscan,
                    documents,
                    embeddings,
                    param1_index,
                    param2_index,
                )
                future_result.add_done_callback(callback)

        for metric in self.metrics:
            np.savetxt(f"data/{metric}_map.csv", metric_maps[metric], delimiter=",")
