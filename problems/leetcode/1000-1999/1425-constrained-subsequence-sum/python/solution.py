"""
https://leetcode.com/problems/constrained-subsequence-sum/description/
271 ms Beats 74.47%
34.89 MB Beats 75.18%
"""

from typing import *


"""
nums = [10,-2,-10,-5,20], k = 2
1. dp[][] dp[i-1][] i (i-1, i-2,... i-k) 
1  dp[i] = nums[i] + max(0, dp[i-1]..dp[i-k])
"""
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        q = deque()

        for i in range(n):
            dp[i] = nums[i] + max(0, q[0] if q else 0)
            if q and i - k >= 0 and q[0] == dp[i - k]:
                q.popleft()
            while len(q) > 0 and q[-1] < dp[i]:
                q.pop()
            q.append(dp[i])
        return max(dp)
