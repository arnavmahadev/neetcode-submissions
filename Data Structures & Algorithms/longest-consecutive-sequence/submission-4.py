class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sequences = []
        numset = set(nums)
        for num in numset:
            if num - 1 not in numset:
                sequence = [num]
                while num + 1 in numset:
                    sequence.append(num + 1)
                    num += 1
                sequences.append(sequence)
        max_length = max(len(seq) for seq in sequences)
        return max_length
