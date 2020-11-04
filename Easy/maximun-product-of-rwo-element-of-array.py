# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        result = []
        product = 1
        for i in range(0, length):
            for j in range(i+1, length):
                product = (nums[i] - 1) * (nums[j] - 1)
                result.append(product)

        return max(result)