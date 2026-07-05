import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while r >= l:
            currIndex = (r + l) // 2
            if target < nums[currIndex]:
                r = currIndex - 1
            elif target >  nums[currIndex]:
                l = currIndex + 1
            elif target == nums[currIndex]:
                return currIndex
        return -1