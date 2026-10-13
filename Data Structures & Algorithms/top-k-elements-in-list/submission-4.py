class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        
        for key, val in dict.items():
            freq[val].append(key)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

