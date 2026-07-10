class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))
            result += "*"
            result += string
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j])
            i = j + 1
            result_str = s[i:i+length]
            result.append(result_str)
            i += length
        return result