def test_benchmark_basic(benchmark) -> None:
    """A basic benchmark test for Python."""
    def basic_operation():
        return sum(range(100))
    benchmark(basic_operation)
