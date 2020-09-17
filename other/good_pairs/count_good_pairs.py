def count_good_pairs(nums: list) -> int:
    pairs = {}
    counter = 1
    for index, num in enumerate(nums):
        pairs[index] = nums[counter:].count(num)
        counter += 1
    return sum(pairs.values())

