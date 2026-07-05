class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        length = 1
        res = 0
        for num in nums:
            numSet.add(num)

        for num in nums:
            if num - 1 not in numSet:
                while num + 1 in numSet:
                    length += 1
                    num += 1
                res = max(res, length)
                length = 1
        return res
                    