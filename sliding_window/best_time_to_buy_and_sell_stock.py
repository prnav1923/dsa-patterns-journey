"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Pattern: Sliding Window / Two Pointers

Approach: One Pass (O(n))
1. Track the minimum price seen so far.
2. For each day, calculate the potential profit (current price - min price).
3. Update the maximum profit if the current profit is higher.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 # l is buy, r is sell
        max_p = 0
        
        while r < len(prices):
            # Is this a profitable trade?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r # Found a lower price point to buy
            r += 1
            
        return max_p
