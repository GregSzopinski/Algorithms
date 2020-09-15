def two_sum(nums: list[int], target: 'int') -> list[int]:
    values = {}
    for index, num in enumerate(nums):
        comp = target - num
        if comp in values:
            return [values[comp], index]
        values[num] = index
        return []
