class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        jin = 1
        for i in range(length-1, -1, -1):
            cur = digits[i] + jin
            digits[i] = cur % 10
            jin = cur // 10
        if jin == 1:
            digits = [1] + digits
        return digits

# if __name__ == '__main__':
#     so = Solution()
#     d = []
#     res = so.plusOne(d)
#     print(res)
