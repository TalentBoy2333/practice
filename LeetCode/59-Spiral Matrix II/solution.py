class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        length = n
        res = [[0 for _ in range(length)] for _ in range(length)]
        top = 0 
        bot = length - 1 
        left = 0 
        right = length - 1
        num = 1
        while top <= bot and left <= right:
            for i in range(left, right+1):
                res[top][i] = num 
                num += 1
            for i in range(top+1, bot+1):
                res[i][right] = num 
                num += 1
            for i in range(right-1, left-1, -1):
                res[bot][i] = num
                num += 1
            for i in range(bot-1, top, -1):
                res[i][left] = num 
                num += 1
            top += 1
            bot -= 1
            left += 1
            right -= 1
        return res 

# so = Solution()
# res = so.generateMatrix(3)
# for l in res:
#     print(l)
            