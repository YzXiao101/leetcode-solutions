"""
https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
13 ms Beats 7.68%
17.69 MB Beats 75.95%
"""

from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def fk(nums1, nums2, l1, r1, l2, r2, k):
            if l1 > r1:
                return nums2[l2 + k - 1]
            if l2 > r2:
                return nums1[l1 + k - 1]
            if k == 1:
                return min(nums1[l1], nums2[l2])

            a, b = (k // 2) + l1 - 1, (k // 2) + l2 - 1
            if a > r1:
                a, b = r1, l2 + (k - (r1 - l1 + 1)) - 1
            elif b > r2:
                a, b = l1 + (k - (r2 + 1 - l2)) - 1, r2

            if nums1[a] < nums2[b]:
                k -= a + 1 - l1
                l1 = a + 1
            else:
                k -= b + 1 - l2
                l2 = b + 1

            return fk(nums1, nums2, l1, r1, l2, r2, k)

        s1, s2 = len(nums1), len(nums2)
        # print(fk(nums1, nums2, 0, s1 - 1, 0, s2 - 1, ((s1 + s2) // 2)))
        # print(fk(nums1, nums2, 0, s1 - 1, 0, s2 - 1, ((s1 + s2) // 2) + 1))
        return (
            fk(nums1, nums2, 0, s1 - 1, 0, s2 - 1, ((s1 + s2) // 2) + 1)
            if (s1 + s2) % 2 == 1
            else (
                fk(nums1, nums2, 0, s1 - 1, 0, s2 - 1, (s1 + s2) // 2)
                + fk(nums1, nums2, 0, s1 - 1, 0, s2 - 1, ((s1 + s2) // 2) + 1)
            )
            / 2
        )
