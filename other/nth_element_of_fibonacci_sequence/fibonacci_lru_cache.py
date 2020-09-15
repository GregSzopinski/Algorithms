from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n: int) -> int:
    """Improved implementation using python's built-in caching"""
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
