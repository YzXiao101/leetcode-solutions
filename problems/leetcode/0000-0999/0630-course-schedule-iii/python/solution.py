"""
https://leetcode.cn/problems/course-schedule-iii/description/
27 ms 击败 86.34%
21.33 MB 击败 18.05%
"""

from typing import *


import heapq
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        watermark = 0
        max_heap = []

        courses.sort(key=lambda x: x[1])
        for course in courses:
            if watermark + course[0] <= course[1]:
                watermark += course[0]
                heapq.heappush(max_heap, -1 * course[0])
            elif len(max_heap) > 0 and (max_heap[0] + course[0] < 0):
                watermark -= -max_heap[0] - course[0]
                # heapq.heappop(max_heap)
                heapq.heapreplace(max_heap, -1 * course[0])
        return len(max_heap)
