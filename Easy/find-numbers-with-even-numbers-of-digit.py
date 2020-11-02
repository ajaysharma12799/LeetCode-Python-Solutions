# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        globalCounter = 0
        for num in nums:
            temp = num
            count = 0
            while(temp != 0):
                temp //= 10
                count += 1
                
            if count % 2 == 0:
                globalCounter += 1
        
        return globalCounter