"""
https://leetcode.com/problems/sliding-window-maximum/description/
167 ms Beats 82.77%
35.38 MB Beats 37.38%
"""

from typing import *

"""
[9,10,9,-7,-4],-8,2,-6
9,[10,9,-7,-4,-8],2,-6
[9],10,[9,-7,-4,-8,2],-6
9,10,9,[-7,-4,-8,2,-6]

10 9 -4 -> 10
10 9 -4 -8 -> 10
9 2 -> 9
9 2 -6 -> 9

[-7,-8,7,5,[7,1,6,0]
k = 4
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, n = [], len(nums)
        q = deque()
        for i in range(k):
            while len(q) > 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        ans.append(q[0])
        for i in range(k, n):
            if q[0] == nums[i - k]:
                q.popleft()
            while len(q) > 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans
