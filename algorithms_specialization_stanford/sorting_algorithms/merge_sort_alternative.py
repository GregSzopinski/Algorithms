def merge(left_x, right_x):
    """Implementation of merge subroutine"""
    x = []
    # traversing through left half of x
    i = 0
    # traversing through right half of x
    j = 0

    # merging step
    # populate x with smaller element from pair of sub-lists
    while i < len(left_x) and j < len(right_x):
        if left_x[i] < right_x[j]:
            x.append(left_x[i])
            i += 1
        else:
            x.append(right_x[j])
            j += 1

    # go through each of sub-lists if there are any elements left
    if i == len(left_x):
        x.extend(right_x[j:])
    else:
        x.extend(left_x[i:])
    return x


def merge_sort(x):
    """Short and clean implementation of merge sort"""
    if len(x) <= 1:
        return x
    else:
        left_x = merge_sort(x[:len(x)//2])
        right_x = merge_sort(x[len(x)//2:])
        return merge(left_x, right_x)

