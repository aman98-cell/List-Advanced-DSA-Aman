class Solution:
    def maxxProfit(self,prices):
        # Time: O(N^2) (Brute Force)
        # Space: O(1)
        max_profit = 0
        days = len(prices)
        # i is buying pointer
        # j is selling pointer

        for i in range(days):
            for j in range(i+1, days):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(profit, max_profit)

        return max_profit

    def  maxxProfitEff(self,prices):
        # Time: O(n)
        # Space: O(1)
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            #finding the minimum price here
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        return max_profit


solution1 = Solution()
prices = [7,1,5,3,6,4]
print(solution1.maxxProfitEff(prices))


