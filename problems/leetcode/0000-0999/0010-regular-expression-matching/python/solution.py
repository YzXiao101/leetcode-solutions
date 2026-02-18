"""
https://leetcode.cn/problems/regular-expression-matching/description/
64 ms Beats 10.74%
15.03 MB Beats 100.00%
"""

from typing import *


"""
1 dp
2 * 
3 -
4 
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1, n2 = len(s), len(p)
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        def match(i, j):
            nonlocal s, p
            return s[i] == p[j] or p[j] == "."

        # base
        dp[0][0] = True
        for j in range(1, n2 + 1):
            if p[j - 1] == "*":
                dp[0][j] |= dp[0][j - 2]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if match(i - 1, j - 1):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 0
                    if 0 <= j - 2:
                        dp[i][j] |= dp[i][j - 2]
                    # >=1
                    dp[i][j] |= match(i - 1, j - 2) and dp[i - 1][j]
                # else:
        return dp[n1][n2]
