"""
 K’th largest element in a stream
Given an infinite stream of integers, find the k’th largest element at any point of time.

"""

import heapq

class Solution:
    @staticmethod
    def find_kth(stream, pos, size):
        curr = 0
        window = []
        for item in stream:
            if curr < size:
                heapq.heappush(window, item)
            else:
                heapq.heappushpop(window, item)
            if curr == pos:
                return window
            curr += 1
        return window

def test_solution():
    stream = [1,3,5,56,23,46,24,54,3,12,53,5,6,9, 234,2,6,7]
    kth = Solution.find_kth(stream, 14, 5)
    print(kth)


test_solution()