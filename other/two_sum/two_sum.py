from typing import List


def two_sum(nums: List[int], target: 'int') -> List[int]:
    """
    A solution to leetcode's two sum problem
    https://leetcode.com/problems/two-sum/
    """
    values = {}
    for index, num in enumerate(nums):
        comp = target - num
        if comp in values:
            return [values[comp], index]
        values[num] = index
        return []
