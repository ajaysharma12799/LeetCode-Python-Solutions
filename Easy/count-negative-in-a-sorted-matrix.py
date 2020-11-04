# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for sublist in grid:
            length = len(sublist)
            for i in range(length):
                if sublist[i] < 0:
                    count += 1
        return count