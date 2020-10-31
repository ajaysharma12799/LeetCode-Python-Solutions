# https://leetcode.com/problems/shuffle-the-array/

# Note :- This Problem is Done using Thidr Pointer

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)
        shuffle = [0 for i in range(length)] # Creating Empty Array of Complete Array Length
        i = 0
        j = n
        current = 0
        
        while(i < n):
            shuffle[current] = nums[i]
            current += 1
            i += 1
            
            shuffle[current] = nums[j]
            current += 1
            j += 1
        return shuffle