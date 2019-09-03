class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if -0.00001 <= x <= 0.00001:
            return 0
        if abs(x) != 1 and n <= -2147483648:
            return 0
        if n < 0:
            flag = -1
            n = -1 * n
        else:
            flag = 1
        res = self.part(x, n)
        return res ** flag

    def part(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 1:
                return -1 
            else:
                return 1
        if n % 2 == 0:
            return self.part(x, n // 2) * self.part(x, n // 2)
        else:
            return self.part(x, n // 2) * self.part(x, n // 2) * x