"""
https://leetcode.com/problems/max-value-of-equation/description/
xx ms Beats xx%
xx MB Beats xx%
"""

"""
(xi, yi) (xj, yj)
xj+yj + (yi-xi)
1. 等式变形
2. 滑动窗口 [1 4 8] (x,y) [1, k]
1 2 3 2 5 2 1 3 1
5 3 1
"""
from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = deque()
        n = len(points)
        ans = -inf
        for i in range(n):
            while q and points[i][0] - points[q[0]][0] > k:
                q.popleft()
            ans = max(
                ans,
                (
                    (points[i][0] + points[i][1] - points[q[0]][0] + points[q[0]][1])
                    if q
                    else ans
                ),
            )
            while q and (
                points[q[-1]][1] - points[q[-1]][0] < points[i][1] - points[i][0]
            ):
                q.pop()
            q.append(i)
        return ans
