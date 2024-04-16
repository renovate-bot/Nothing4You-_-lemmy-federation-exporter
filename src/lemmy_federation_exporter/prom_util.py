from collections.abc import Iterable

from prometheus_client.core import CollectorRegistry, Metric
from prometheus_client.exposition import generate_latest
from prometheus_client.registry import Collector


class CollectorHelper(Collector):
    metrics: dict[str, Metric]

    def __init__(self) -> None:
        self.metrics = {}

        self.registry = CollectorRegistry(auto_describe=True)
        self.registry.register(self)

    def add_metric(self, metric: Metric) -> None:
        if metric.name in self.metrics:
            raise ValueError(f"{metric.name} metric was already added")

        self.metrics[metric.name] = metric

    def collect(self) -> Iterable[Metric]:
        yield from self.metrics.values()

    def generate(self) -> bytes:
        return generate_latest(self.registry)
