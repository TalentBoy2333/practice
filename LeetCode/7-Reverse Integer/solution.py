class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0] == '-':
            s = s[1:]
        s = s[::-1]
        if x < 0:
            res = -1 * int(s)
        else:
            res = int(s)
        if -2**31 < res < 2**31-1:
            return res 
        else:
            return 0

        

# if __name__ == '__main__':
#     x = -123
#     so = Solution()
#     res = so.reverse(x)
#     print(res)