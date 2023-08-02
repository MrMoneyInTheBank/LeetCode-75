'''
You are given an array prices where prices[i] is the price 
of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.
'''
def maxProfit(prices):

    min_price, max_profit = float('inf'), 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        max_profit =  max(max_profit, prices[i] - min_price)
            
    return max_profit
    

# The idea is the find the minimum price and maximum price such that the minimum 
# price occurs before the maximum prices. At each iteration, the minimum price 
# ending on the current day is being updated. The potential profit of selling 
# on a day is checked. If there is a day later which increases the profit, the profit
# will be adjusted accordingly. We could do this using two loops by utlizing kadane's 
# algorithm to find the minimum price ending on every day, calculting the profit from selling
# on every day, and then taking the maximum profit. 

# Time | Space: O(n) | O(n)

