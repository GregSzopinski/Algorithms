# Put it outside the function to avoid recursion
fibonacci_cache = {}


def fibonacci(n: int) -> int:
    """Improve implementation using custom, basic caching"""
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n in [1, 2]:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = value
    return value
