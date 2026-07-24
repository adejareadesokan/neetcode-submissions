class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(lst, num, offset):
            left, right = 0, len(lst) - 1
            while left <= right:
                mid = (left + right) // 2
                if lst[mid] == num:
                    return mid + offset  
                elif lst[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        index = left  

        result = binary_search(nums[:index], target, 0)
        if result != -1:
            return result
        return binary_search(nums[index:], target, index)