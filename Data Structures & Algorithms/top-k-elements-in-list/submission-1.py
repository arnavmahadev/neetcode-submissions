class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first im going to create a hashmap and iterate through 
        #nums using num as keys and freq as values. then im going 
        #to extract everything from the hashmap using .items() 
        #and add it to an array but backwards. then i will sort 
        #the array. then i will get the first k entries and append 
        #their values to a result array.

        result = []
        array = []

        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0) #freq of each num
        for num, freq in dict.items():
            array.append([freq, num])
        array.sort()
        
        while len(result) < k:
            result.append(array.pop()[1])

        return result
        