'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


def climbStairs(n):
    one, two = 1, 1

    for _ in range(n-1):
        tmp = one
        one += two
        two = tmp

    return one

# If we work backwards, there is one way to go form n to n and one way to go form n-1 to n.
# There are two ways to go from n-2 to n (via n-1 and direct). If we continue to this pattern,
# We will find that we always add the number of ways of the previous and the one before that. This
# is essentially the fibonacci sequence. We only range until n-1 because we need to fill in n-2 spots
# and the range function iterates until the second last position

# Time | Space: O(n) | O(1)
