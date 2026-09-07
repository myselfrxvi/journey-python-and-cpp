# LeetCode 26: Remove Duplicates from Sorted Array (Easy)
# Pattern: In-Place Two Pointers (Reader & Writer)
# Time Complexity: O(N), Space Complexity: O(1)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    k = s.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")
