from random import shuffle
from merge_sort_alternative import merge_sort

test_input = list(range(1, 100))
shuffle(test_input)
# print(test_input)
print(merge_sort(test_input))