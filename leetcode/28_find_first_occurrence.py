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
    print("Test 1:", s.strStr("sadbutsad", "sad"))
    print("Test 2:", s.strStr("leetcode", "leeto"))
