# https://leetcode.com/problems/number-of-good-pairs/


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count