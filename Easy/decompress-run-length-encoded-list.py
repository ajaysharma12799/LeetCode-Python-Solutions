# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        tempList = []
        decompress = []
        length = len(nums) // 2
        
        for i in range(length):
            tempList.append([nums[2*i], nums[2*i+1]])
        
        for sublist in tempList:
            for i in range(sublist[0]):
                decompress.append(sublist[1])
            
        return decompress