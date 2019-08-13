'''
给定一个三角形，找出从顶到底的最小路径和，每一步可以从上一行移动到下一行相邻的数字
[                   
    [2],                [2],              
    [3,4],              [3, 4],             [2],
    [6,5,7],      ==>   [7, 6, 10]     ==>  [9, 10]   ==>     [11]
    [4,1,8,3]
]
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == []:
            return 0
        dep = len(triangle)
        for i in range(dep-2, -1, -1):
            num = len(triangle[i])
            for j in range(num):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

# t = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# so = Solution()
# res = so.minimumTotal(t)
# print(res)