"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of 
money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

"""

def coinChange(coins, amount):
    dp = [float("inf")] * (amount+1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            else:
                dp[i] = min(dp[i], 1+dp[i-coin]) 
    
    return dp[-1] if dp[-1] != float("inf") else -1

# Time | Space: O(n) | O(1)

# We start from computing how many coins are needed to make $1. If this can't be done, then the
# cache will hold a default value. For creating $x, for each coin $c, we need to be able to create
# $x - c. Therefore, dp[x] = min(dp[x], 1 + dp[x-c] for c in coins). We are adding 1 since we are 
# taking the current coin into account. If dp[-1] == default by the end of the loop, then we are unable
# to make the current amount regardless of how many coins we use and therefore we can return -1. 
