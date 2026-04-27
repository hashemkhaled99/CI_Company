"""Benchmark test for Python."""

from pytest_benchmark.fixture import BenchmarkFixture


def test_benchmark_basic(benchmark: BenchmarkFixture) -> None:
    """A basic benchmark test for Python."""
    def basic_operation() -> int:
        return sum(range(100))

    benchmark(basic_operation)


