# https://leetcode.com/problems/matrix-diagonal-sum/

"""
Approach One Works on O(n^2) Solution
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matSum = 0
        length = len(mat)
        primary, secondary = 0, 0

        for i in range(0, length):
            for j in range(0, length):
                if i == j:
                    primary += mat[i][j]
            
                if i + j == length - 1:
                    secondary += mat[i][j]
        
        matSum = primary + secondary

        if length % 2 != 0:
            Number_of_Elements = length * length
            Row_Col = length + length
            idx = Number_of_Elements // Row_Col
            matSum -= mat[idx][idx]
        return matSum

"""
Approach Two Works on O(n) Solution
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matSum = 0
        length = len(mat)
        primary, secondary = 0, 0

        for i in range(0, length):
            primary = mat[i][i]
            secondary = mat[i][length-i-1]

        matSum = primary + secondary

        if length % 2 != 0:
            Number_of_Elements = length * length
            Row_Col = length + length
            idx = Number_of_Elements // Row_Col
            matSum -= mat[idx][idx]
        return matSum