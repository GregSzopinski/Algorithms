def count_good_pairs(nums: list) -> int:
    hash_map = {}
    res = 0

    for number in nums:
        if number in hash_map:
            res += hash_map[number]
            hash_map[number] += 1
        else:
            hash_map[number] = 1

    return res

