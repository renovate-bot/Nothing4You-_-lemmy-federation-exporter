from prometheus_client.core import Metric, CollectorRegistry
from prometheus_client.exposition import generate_latest
from prometheus_client.registry import Collector


class CollectorHelper(Collector):
    def __init__(self):
        self.metrics = {}

        self.registry = CollectorRegistry(auto_describe=True)
        self.registry.register(self)

    def add_metric(self, metric: Metric):
        if metric.name in self.metrics:
            raise ValueError(f"{metric.name} metric was already added")

        self.metrics[metric.name] = metric

    def collect(self):
        for metric in self.metrics.values():
            yield metric

    def generate(self):
        return generate_latest(self.registry)
