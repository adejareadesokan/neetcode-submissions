class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        norm_xor = 0
        acc_xor = 0
        for i in range(len(nums)+ 1):
            norm_xor ^= i
        for j in range(len(nums)):
            acc_xor ^= nums[j]
        return norm_xor ^ acc_xor

        