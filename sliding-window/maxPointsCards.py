"""
Problem - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        len_cards = len(cardPoints)
        sum_left, sum_right = sum(cardPoints[:k]), 0
        res = sum_left
        for i in range(k):
            sum_left -= cardPoints[k - 1 - i]
            sum_right += cardPoints[len_cards - 1 - i]
            res = max(res, sum_left + sum_right)
        return res


print(Solution().maxScore([2, 6], 1))
