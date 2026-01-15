"""
Problem - https://leetcode.com/problems/contains-duplicate-iii/
"""

from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        seen = {}
        bucktSize = valueDiff if valueDiff else 1
        for i, val in enumerate(nums):
            buckt = val // bucktSize
            if (
                buckt in seen
                and abs(i - seen[buckt]) <= indexDiff
                and abs(val - nums[seen[buckt]]) <= valueDiff
            ):
                return True
            elif (
                buckt - 1 in seen
                and abs(i - seen[buckt - 1]) <= indexDiff
                and abs(val - nums[seen[buckt - 1]]) <= valueDiff
            ):
                return True
            elif (
                buckt + 1 in seen
                and abs(i - seen[buckt + 1]) <= indexDiff
                and abs(val - nums[seen[buckt + 1]]) <= valueDiff
            ):
                return True

            seen[buckt] = i

        return False


print(Solution().containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
