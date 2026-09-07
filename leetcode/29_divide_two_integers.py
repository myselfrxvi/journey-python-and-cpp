class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negative = (dividend < 0) ^ (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            quotient += multiple

        return -quotient if negative else quotient

if __name__ == "__main__":
    s = Solution()
    print("10 / 3 =", s.divide(10, 3))
    print("7 / -3 =", s.divide(7, -3))
