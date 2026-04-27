import typing

def test_benchmark_basic(benchmark: typing.Any) -> None:
    """A basic benchmark test for Python."""
    def basic_operation() -> int:
        return sum(range(100))
    benchmark(basic_operation)

