class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [] 
        elif numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(1, numRows):
            cur = [0 for _ in range(i+1)]
            cur[0] = cur[-1] = 1
            for j in range(1, len(cur)-1):
                cur[j] = res[-1][j-1] + res[-1][j]
            res.append(cur)
        return res

# if __name__ == '__main__':
#     so = Solution()
#     res = so.generate(5)
#     print(res)