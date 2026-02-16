class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        t0, t1, t2 = 0, 1, 1
        for _ in range(2, n):
            t2, t1, t0 = t2 + t1 + t0, t2, t1
        return t2


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        t0, t1, t2 = 0, 1, 1
        for _ in range(2, n):
            t2, t1, t0 = t2 + t1 + t0, t2, t1
        return t2


# * make it faster by using a dp array, then we won't need to re-assign t1 & t0