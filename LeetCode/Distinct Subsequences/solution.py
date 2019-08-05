'''
解题思路: 
https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-by-powcai-5/

动态规划
dp[i][j] 代表 T 前 i 字符串可以由 S 前 j 字符串组成最多个数.
所以动态方程:
当 S[j] == T[i] , dp[i][j] = dp[i-1][j-1] + dp[i][j-1];
当 S[j] != T[i] , dp[i][j] = dp[i][j-1]
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == '':
            return 0 
        if t == '':
            return 1
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(t)+1)]
        for i in range(0, len(s)+1):
            dp[0][i] = 1 
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

# if __name__ == '__main__':
#     s = "babgbag"
#     t = "bag"
#     so = Solution()
#     so.numDistinct(s, t)