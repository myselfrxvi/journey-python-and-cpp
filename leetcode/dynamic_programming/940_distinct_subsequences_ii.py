class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = {}

        for ch in s:
            new_a = (total + 1) % MOD
            diff = (new_a - last.get(ch, 0) + MOD) % MOD
            last[ch] = new_a
            total = (total + diff) % MOD
        return total

if __name__ == "__main__":
    sol = Solution()
    print("aba:", sol.distinctSubseqII("aba"))
    print("abc:", sol.distinctSubseqII("abc"))
    print("aaa:", sol.distinctSubseqII("aaa"))
