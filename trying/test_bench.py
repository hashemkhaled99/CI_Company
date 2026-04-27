"""Benchmark test for Python."""

from pytest_benchmark.fixture import BenchmarkFixture

from trying.logic import calculate_status


def test_benchmark_basic(benchmark: BenchmarkFixture) -> None:
    """A basic benchmark test for Python."""
    benchmark(calculate_status, 100)


