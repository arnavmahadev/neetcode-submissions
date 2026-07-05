class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            for x in range(i):
                mini = min(prices[x], mini)
            maxi = prices[i] - mini
            res = max(res, maxi)
        return res