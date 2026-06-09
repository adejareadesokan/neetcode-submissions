class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_cpy = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    num_cpy.append(i)
                    num_cpy.append(j)
        return num_cpy
        
            
        