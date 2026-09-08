class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in mapping:
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack
