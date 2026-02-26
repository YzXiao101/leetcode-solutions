"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
xx ms Beats xx%
xx MB Beats xx%
"""

from typing import *


from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n, ps = len(nums), [0] * (len(nums) + 1)
        if n == 1:
            return 1 if nums[0] >= k else -1
        for num in nums:
            if num >= k:
                return 1
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]
        print(ps)
        q = deque([n - 1])
        ans = inf
        for i in range(n - 2, -1, -1):
            while q and ps[q[-1] + 1] - ps[i + 1 - 1] >= k:
                ans = min(ans, q[-1] - i + 1)
                q.pop()
            while q and ps[q[0] + 1] <= ps[i + 1]:
                q.popleft()
            q.appendleft(i)
        return -1 if ans == inf else ans
