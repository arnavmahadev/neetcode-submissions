class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while abs(x) > 0:
            temp = x % 10 if x > 0 else x % -10
            res = res*10 + temp
            x = int(x / 10)
        if (res > (2**31 - 1) or res < -2**31):
            return 0
        return res