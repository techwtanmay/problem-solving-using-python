"""
Problem - https://leetcode.com/problems/contains-duplicate-ii/description/
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = set()

        for i, val in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])

            if val in seen:
                return True

            seen.add(val)

        return False
