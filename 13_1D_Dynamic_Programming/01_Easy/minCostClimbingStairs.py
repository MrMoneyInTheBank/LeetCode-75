"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

def minCostClimbingStairs(cost):
    cost.append(0)
    cost.append(0)

    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])

    return min(cost[:2])

# Time | Space: O(n) | O(1)

# the minimum is the cost you pay currently + the minimum path from where 
# you can jump to. Working backwards, we can use dynammic programming to fill the cost to reach
# the end from each position. Then, we can return the minimum of the first two elements. 
