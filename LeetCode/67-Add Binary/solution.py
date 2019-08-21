class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == '':
            return b 
        if b == '':
            return a
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        jin = 0
        while i >= 0 and j >= 0:
            cur = int(a[i]) + int(b[j]) + jin
            res = str(cur % 2) + res 
            jin = cur // 2
            i -= 1
            j -= 1
        # print(res)
        while i >= 0:
            cur = int(a[i]) + jin
            res = str(cur % 2) + res 
            jin = cur // 2
            i -= 1
        # print(res)
        while j >= 0:
            cur = int(b[j]) + jin
            res = str(cur % 2) + res 
            jin = cur // 2
            j -= 1
        # print(res)
        if jin == 1:
            res = '1' + res 
        return res

# if __name__ == '__main__':
#     so = Solution()
#     res = so.addBinary('11', '1')
#     print(res)

            