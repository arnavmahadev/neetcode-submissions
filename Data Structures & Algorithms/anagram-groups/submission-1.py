class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first for each string in strs init an array keeping 
        #track of freq of each letter. add these arrays, and 
        #the word to a hashmap and return the .values() of the hashmap.
        
        result = {}
        
        for str in strs:
            strList = [0] * 26
            for c in str:
                strList[ord(c) - ord('a')] += 1
            strTuple = tuple(strList)
            result.setdefault(strTuple, []).append(str)
        return list(result.values())