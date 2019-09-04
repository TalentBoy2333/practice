class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        h = len(matrix)
        w = len(matrix[0])
        res = []

        top = 0 
        bot = h-1 
        left = 0 
        right = w-1
        while top <= bot and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, bot+1):
                res.append(matrix[i][right])
            if top < bot:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bot][i])
            if left < right:
                for i in range(bot-1, top, -1):
                    res.append(matrix[i][left])
            top += 1
            bot -= 1
            left += 1
            right -= 1
        return res

# mat = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# so = Solution()
# res = so.spiralOrder(mat)
# print(res)