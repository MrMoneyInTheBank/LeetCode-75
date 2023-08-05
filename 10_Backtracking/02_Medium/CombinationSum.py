from typing import List 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, currSum, currPath):
            if currSum > target or idx == len(candidates):
                return
            if currSum == target:
                res.append(currPath.copy())
                return

            # Choose the current number
            backtrack(idx, currSum + candidates[idx], currPath + [candidates[idx]])

            # Don't choose the current number
            backtrack(idx + 1, currSum, currPath)

        backtrack(0, 0, [])
        return res