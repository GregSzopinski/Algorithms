def merge_sort(x: list):
    """
    Python implementation of merge sort algorithm
    Given a list x, split it into smaller sub-lists, sort each one recursively, then merge
    :type x: list
    """
    if len(x) <= 1:
        # if a list is empty or have length of one, return it as it is.
        print("Single number or an empty array. Moving on... ")
    else:
        # splitting step
        middle: int = len(x) // 2
        left_x = x[:middle]
        right_x = x[middle:]
        merge_sort(left_x)
        merge_sort(right_x)

        # traversing through left half of x
        i = 0
        # traversing through right half of x
        j = 0
        # populating merged x
        k = 0

        # merging step
        # populate x with smaller element from pair of sub-lists
        while i < len(left_x) and j < len(right_x):
            if left_x[i] <= right_x[j]:
                x[k] = left_x[i]
                i += 1
            else:
                x[k] = right_x[j]
                j += 1
            k += 1

        # go through each of sub-lists if there are any elements left
        while i < len(left_x):
            x[k] = left_x[i]
            i += 1
            k += 1

        while j < len(right_x):
            x[k] = right_x[j]
            j += 1
            k += 1

    return x

