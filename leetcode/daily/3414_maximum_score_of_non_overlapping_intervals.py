from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        events = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)], key=lambda x: x[1])
        n = len(events)
        end_times = [x[1] for x in events]
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, orig_idx = events[i - 1]
            prev = bisect_left(end_times, l)

            for k in range(1, 5):
                best = dp[i - 1][k]
                prev_weight, prev_indices = dp[prev][k - 1]
                new_weight = prev_weight + w
                new_indices = sorted(prev_indices + [orig_idx])
                
                if new_weight > best[0] or (new_weight == best[0] and new_indices < best[1]):
                    best = (new_weight, new_indices)

                dp[i][k] = best

        return dp[n][4][1]
