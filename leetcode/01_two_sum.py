# LeetCode 01: Two Sum (Easy)
# Pattern: Hash Map (Single Pass)
# Time Complexity: O(N), Space Complexity: O(N)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
