class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return x
        pre, end = 0, x
        while pre < end-1:
            # print(pre, end)
            mid = (pre + end) // 2
            if mid * mid > x:
                end = mid
            else:
                pre = mid

        return pre

# if __name__ == '__main__':
#     so = Solution()
#     res = so.mySqrt(7)
#     print(res)