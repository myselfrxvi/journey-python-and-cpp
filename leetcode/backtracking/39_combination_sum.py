from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        
        candidates.sort()

        def backtrack(start_idx: int, total: int):
            if total == target:
                res.append(list(combo))
                return
            if total > target:
                return

            for i in range(start_idx, len(candidates)):
                if total + candidates[i] > target:
                    break
                combo.append(candidates[i])
                backtrack(i, total + candidates[i])
                combo.pop()
        backtrack(0, 0)
        return res
