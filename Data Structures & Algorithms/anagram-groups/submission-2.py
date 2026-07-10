class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            freq = [0] * 26
            for char in str:
                if freq[ord(char) - 97] > 0:
                    freq[ord(char) - 97] += 1
                else: 
                    freq[ord(char) - 97] = 1
            if tuple(freq) in dict:
                dict[tuple(freq)].append(str)
            else:
                dict[tuple(freq)] = [str]
        return list(dict.values())
        