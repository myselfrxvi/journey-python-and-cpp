class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        start, end = 0, 0
        def expand(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            max_l = max(len1, len2)
            if max_l > end - start:
                start = i - (max_l - 1) // 2
                end = i + max_l // 2
        return s[start:end + 1]
