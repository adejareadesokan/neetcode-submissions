class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        prefix_val = 1
        suffix_val =1
        for i in range(len(nums)):
            prefix[i] = prefix_val
            prefix_val *= nums[i]

            
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suffix_val
            suffix_val *= nums[i]
        product = [prefix[i] *suffix[i] for i in range(len(nums))]
        return product

        