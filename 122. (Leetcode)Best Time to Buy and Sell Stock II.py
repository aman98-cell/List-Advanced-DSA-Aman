from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        days = len(prices)

        for i in range(1, days):
            if prices[i] > prices[i - 1]:
                profit = profit + prices[i] - prices[i - 1]

        return profit


prices = [7,1,5,3,6,4]
days = len(prices)
instance1 = Solution()
print(instance1.maxProfit(prices))