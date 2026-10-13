class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        suffix_arr = [1] * len(nums)
        prefix = suffix = 1
        result = [1] * len(nums)
        for i in range(len(nums) - 1):
            prefix_arr[i+1] *= nums[i] * prefix_arr[i]
        for i in range(len(nums) - 1, 0, -1):
            suffix_arr[i-1] *= nums[i] * suffix_arr[i]
        for i in range(len(nums)):
            result[i] = prefix_arr[i] * suffix_arr[i]
        return result