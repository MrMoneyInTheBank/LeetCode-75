"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.
"""

def main(temps):
    res = [0 for t in temps]
    stack = [] # [idx, temp]

    for idx, t in enumerate(temps):
        while stack and t > stack[-1][1]:
            stackIdx, stackTemp = stack.pop()
            res[stackIdx] = idx - stackIdx
        stack.append([idx, t])
    
    return res

