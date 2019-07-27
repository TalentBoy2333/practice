class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[] for _ in range(n)]
        for temp in dp:
            for _ in range(m):
                temp.append(0)
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # show(dp)
        return dp[n-1][m-1]

# def show(dp):
#     print('dp: ')
#     for temp in dp:
#         print(temp)
#     print()

# if __name__ == '__main__':
#     so = Solution()
#     so.uniquePaths(7, 3)
