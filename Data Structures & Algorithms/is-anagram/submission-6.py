class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        for c in s:
            sMap.update({c: sMap.get(c, 0) + 1})
        for c in t:
            tMap.update({c: tMap.get(c, 0) + 1})
        return sMap == tMap