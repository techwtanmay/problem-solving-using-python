"""
Problem - https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numsHashMap = set()
        for num in nums:
            if num in numsHashMap:
                return True
            else:
                numsHashMap.add(num)

        return False
