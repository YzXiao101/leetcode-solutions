"""
https://leetcode.cn/problems/super-egg-drop/description/
xx ms Beats xx%
xx MB Beats xx%
"""

from typing import *


"""
|-> i
|k  

4
3
2 m
1
0

0

dp[i][j] = min{
    max{
        dp[m-1][j-1],
        dp[i-m][j]
    } + 1
} for m

dp[0][j] = 0
dp[1][j] = min{
    max{
        dp[m-1][j-1],
        dp[i-m][j]
    } + 1
} for m

k = 2, n = 6, o = 0
k = 4, n = 5000
_      _
    _ 
_      _
[1, i]

dp[m][n] m次 n卡
|-> m
n
dp[m][n] = 1 + dp[m-1][n] + dp[m-1][n-1]
dp[m][n] >= t
"""


# import sys;
# from functools import lru_cache
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1)]
        m = 0
        while dp[m][k] < n:
            m += 1
            dp.append([0] * (k + 1))
            for e in range(1, k + 1):
                dp[m][e] = dp[m - 1][e - 1] + dp[m - 1][e] + 1

        return m

    """
        @lru_cache
        def dp(i, j):
            if i == 0:
                return 0
            if j == 1:
                return i
            l, r = 1, i
            while l < r:
                m = (l+r) >> 1
                if dp(m-1,j-1) >= dp(i-m,j):
                    r = m 
                else:
                    l = m+1
            return max(dp(l-1,j-1), dp(i-l,j))+1
        return dp(n, k)
    """
    """
        mv = sys.maxsize
        dp = [[mv]*(k+1) for _ in range(n+1)] # [0,n][0,k]
        # dp[i][1] = i
        for i in range(n+1):
            dp[i][1] = i
        # dp[0][j] = 0
        for j in range(k+1):
            dp[0][j] = 0
        for j in range(2, k+1):
            for i in range(1, n+1):
                # for m in range(1, i+1):
                    # dp[i][j] = min(dp[i][j], max(dp[m-1][j-1], dp[i-m][j])+1)
                l, r = 1, i
                while l < r:
                    m = (l+r) >> 1
                    if dp[m-1][j-1] >= dp[i-m][j]:
                        r = m 
                    else:
                        l = m+1
                dp[i][j] = min(dp[i][j], max(dp[l-1][j-1], dp[i-l][j])+1)
                # print(i, j, dp[i][j])
        return dp[n][k]
    """
