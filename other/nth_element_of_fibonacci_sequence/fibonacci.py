def fibonacci(n: int) -> int:
    """
    Return nth element of Fibonacci sequence.
    This a naive nad slow implementation which serves as a base for further improvements
    """
    # Base case
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
