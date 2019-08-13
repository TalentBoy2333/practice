class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0 
        n = len(matrix[0])
        r = n - 1
        row = 0
        while l < r:
            for i in range(l, r):
                x1, y1 = row, i 
                x2, y2 = y1, n - 1 - x1 
                x3, y3 = y2, n - 1 - x2 
                x4, y4 = y3, n - 1 - x3 
                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4] = \
                matrix[x4][y4], matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]
            row += 1
            l += 1
            r -= 1
        
# if __name__ == '__main__':
#     so = Solution()
#     m = [
#         [ 5, 1, 9,11],
#         [ 2, 4, 8,10],
#         [13, 3, 6, 7],
#         [15,14,12,16]
#       ]
#     so.rotate(m)
#     for l in m:
#         print(l)
