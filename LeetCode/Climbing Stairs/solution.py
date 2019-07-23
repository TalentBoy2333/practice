class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fbnq(n)
        
    def fbnq(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            a, b, i = 1, 2, 2
            while i < n:
                a, b, i = b, a+b, i+1
            return b