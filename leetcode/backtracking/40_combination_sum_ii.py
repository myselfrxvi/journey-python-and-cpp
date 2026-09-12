from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                combo.pop()

        backtrack(0, 0)
        return res
