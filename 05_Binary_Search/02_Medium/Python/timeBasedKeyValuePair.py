"""
Design a time-based key-value data structure that can store multiple 
values for the same key at different time stamps and retrieve the key's 
value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key key with the 
value value at the given time timestamp.

String get(String key, int timestamp) Returns a value such that set was called 
previously, with timestamp_prev <= timestamp. If there are multiple such values, 
it returns the value associated with the largest timestamp_prev. If there are no 
values, it returns "".
"""

import collections

class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, vals = 0, self.store[key]
        l, r = 0, len(vals) - 1 

        while l <= r:
            mid = (l + r) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            elif vals[mid][0] > timestamp:
                r = mid - 1
        return res
