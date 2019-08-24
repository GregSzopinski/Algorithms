def merge_sort(x: list):
    """
    Python implementation of merge sort algorithm
    :type x: list
    """
    print("Splitting... ", x)
    if len(x) <= 1:
        # if a list is empty or have length of one, return it as it is.
        print("Single number. Moving on... ")
    else:
        # splitting step
        middle: int = len(x) // 2
        left_x = x[:middle]
        right_x = x[middle:]
        merge_sort(left_x)
        merge_sort(right_x)

        i = 0
        j = 0
        k = 0

        while i < len(left_x) and j < len(right_x):
            if left_x[i] <= right_x[j]:
                x[k] = left_x[i]
                i += 1
            else:
                x[k] = right_x[j]
                j += 1
            k += 1

        while i < len(left_x):
            x[k] = left_x[i]
            i += 1
            k += 1

        while j < len(right_x):
            x[k] = right_x[j]
            j += 1
            k += 1

    print("Merging... ", x)


# test
print(merge_sort([5, 1, 3.3, 2.1, 1.1, 6, 4]))
print(merge_sort([2, 1, 3, 1, 4, 5, 6, 1, 8, 99, 37, 101, 12, 9.9]))
