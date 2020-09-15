def insertion_sort(a: list) -> list:
    """A cleaner and maybe more pythonic implementation of insertion sort"""
    for i in range(1, len(a)):
        value_to_sort = a[i]
        print(a)
        while i > 0 and a[i-1] > value_to_sort:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    return a