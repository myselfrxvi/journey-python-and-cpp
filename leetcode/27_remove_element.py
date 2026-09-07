# LeetCode 27: Remove Element (Easy)
# Pattern: In-Place Two Pointers (Filtering)
# Time Complexity: O(N), Space Complexity: O(1)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for num in nums:
            if num != val:
                nums[slow] = num
                slow += 1
        return slow

if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    s = Solution()
    k = s.removeElement(nums, 2)
    print(f"k = {k}, nums = {nums[:k]}")
