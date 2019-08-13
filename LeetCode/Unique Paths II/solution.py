class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        dp = [[0 for _ in range(w)] for _ in range(h)]
        for i in range(h):
            if obstacleGrid[i][0] == 1:
                break 
            dp[i][0] = 1
        for i in range(w):
            if obstacleGrid[0][i] == 1:
                break 
            dp[0][i] = 1
        # print(dp)
        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i-1][j] == 1:
                    dp[i][j] = dp[i][j-1]
                elif obstacleGrid[i][j-1] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[h-1][w-1]