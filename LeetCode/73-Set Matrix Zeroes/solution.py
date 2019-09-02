class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h = len(matrix)
        w = len(matrix[0])
        r = set()
        l = set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    r.add(i)
                    l.add(j)
        for i in range(h):
            for j in range(w):
                if i in r or j in l:
                    matrix[i][j] = 0 
        
# matrix = [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# so = Solution()
# so.setZeroes(matrix)
# print(matrix)