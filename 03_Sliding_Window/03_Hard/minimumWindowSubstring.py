from collections import defaultdict


def inside(chars, window):
    for key, value in chars.items():
        if key not in window or window[key] == 0:
            return False
        elif window[key] < value:
            return False

    return True


def minWindow(s, t):
    tCount = defaultdict(int)
    for char in t:
        tCount[char] += 1

    windowCount = defaultdict(int)
    res = ""
    l = 0

    for r in range(len(s)):
        windowCount[s[r]] += 1

        while inside(tCount, windowCount):
            windowCount[s[l]] -= 1
            l += 1

            #res = s[l-1:r+1]
            if res == "" or len(res) > len(s[l-1:r+1]):
                res = s[l-1:r+1]

    return res
