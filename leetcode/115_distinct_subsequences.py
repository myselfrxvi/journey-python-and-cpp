class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)
            return memo[(i, j)]
        return dfs(0, 0)

if __name__ == "__main__":
    s = Solution()
    print("Distinct:", s.numDistinct("rabbbit", "rabbit"))
