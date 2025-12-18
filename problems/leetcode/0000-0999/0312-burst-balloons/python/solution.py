"""
https://leetcode.cn/problems/burst-balloons/
2464 ms Beats 84.02%
19.34 MB Beats 85.95%
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums[:] + [1]
        ln = len(nums)
        dp = [[0] * ln for _ in range(ln)]

        for j in range(1, ln):
            for i in range(j - 1, -1, -1):
                if i + 1 == j:
                    dp[i][j] = 0
                    continue

                res = -1
                for m in range(i + 1, j):
                    res = max(res, nums[i] * nums[m] * nums[j] + dp[i][m] + dp[m][j])
                dp[i][j] = res

        return dp[0][ln - 1]
