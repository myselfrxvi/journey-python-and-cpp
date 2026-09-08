class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        idx = 0
        if s[0] == '-':
            sign = -1
            idx += 1
        elif s[0] == '+':
            idx += 1
        res = 0
        while idx < len(s) and s[idx].isdigit():
            res = res * 10 + int(s[idx])
            idx += 1
        res *= sign
        res = max(-2147483648, min(res, 2147483647))
        return res
