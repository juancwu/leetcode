from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        choose one day to buy, buy with less cost
        coose one day to sell, sell with highest price
        
        init buy cost as inf and select the minimum
        init sell price as -inf and select the maximum
        
        [7,1,5,3,6,4]
         ^ ^
         b s
         s - b < 0 we skip
         [7,1,5,3,6,4]
            ^ ^
            b s
            
            b = min(b, proces[i]) where i is the index of the current cost
            b - s > 0 we keep selling price
            
        [7,1,5,3,6,4]
           ^     ^
           b     s keep this selling price
        [7,1,5,3,6,4]
           ^       ^
           b       s discard
           
        """
        
        if len(prices) == 1:
            return 0
        
        buy_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            else:
                sell_price = prices[i]
                profit = max(sell_price - buy_price, profit)
        
        return profit
            
        
        
        
        