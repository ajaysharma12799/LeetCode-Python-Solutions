# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        XOR_Result = 0
        for i in range(n):
            nums.append(start + 2 * i)

        for i in range(len(nums)):
            XOR_Result ^= nums[i]
        return XOR_Result
