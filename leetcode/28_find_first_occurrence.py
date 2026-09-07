# LeetCode 28: Find the Index of the First Occurrence in a String (Easy)
# Pattern: Sliding Window / String Matching
# Time Complexity: O((N - M + 1) * M), Space Complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print("Test 1:", s.strStr("sadbutsad", "sad"))  # 0
    print("Test 2:", s.strStr("leetcode", "leeto"))  # -1
