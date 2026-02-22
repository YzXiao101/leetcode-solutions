"""
https://leetcode.com/problems/find-latest-group-of-size-m/description/
xx ms Beats xx%
xx MB Beats xx%
"""

"""
0000000000000
0111010111110
0111010110110
互不相同
m
111
 111
  111
-1[ ]-1[ ]-1[ ]-1
-1[  ]-1[  ]-1
4. 只看左边界和右边界
[r l]1
[r l]1[r l]
"""


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return m
        ls = [[1] * 2 for _ in range(n)]  # l->,r<-
        nums = [0] * n
        ans = -1
        for i in range(n):
            j = arr[i] - 1
            nums[j] = 1
            if j + 1 < n and nums[j + 1]:
                ls[j][0] = ls[j + 1][0] + 1
                if ls[j + 1][0] == m:
                    ans = i - 1 + 1
            if j - 1 >= 0 and nums[j - 1]:
                ls[j][1] = ls[j - 1][1] + 1
                if ls[j - 1][1] == m:
                    ans = i - 1 + 1
            if j - 1 >= 0 and nums[j - 1]:
                ls[j - ls[j - 1][1]][0] += ls[j][0]
            if j + 1 < n and nums[j + 1]:
                ls[j + ls[j + 1][0]][1] += ls[j][1]
        return ans
