# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        length = len(nums)
        
        for i in range(length):
            target.insert(index[i], nums[i])
        
        return target
        