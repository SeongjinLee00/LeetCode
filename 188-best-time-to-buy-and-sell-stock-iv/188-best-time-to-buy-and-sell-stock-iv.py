class Solution:
    def maxProfit(self, k, prices):
        if k > len(prices) >> 1: 
            return sum(prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i])
        cash, asset = [float('-inf')] * (k+1), [0] * (k+1)
        for price in prices:
            for i in range(1,k+1):
                cash[i] = max(cash[i], asset[i-1]-price)
                asset[i] = max(asset[i], cash[i]+price)
        return asset[k]