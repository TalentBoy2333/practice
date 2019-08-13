class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = grid 
        temp = 0
        for i in range(len(grid)):
            dp[i][0] = grid[i][0] + temp
            temp = dp[i][0]
        temp = 0
        for i in range(len(grid[0])):
            dp[0][i] = grid[0][i] + temp
            temp = dp[0][i]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        # print(dp)
        return dp[-1][-1]
    
# if __name__ == '__main__':
#     a = [[1,3,1],[1,5,1],[4,2,1]]
#     print(a)
#     so = Solution()
#     res = so.minPathSum(a)
#     print(res)