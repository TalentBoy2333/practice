'''
动态规划:
dp[i][j] 表示 word1前i个字符转换为word2前j个字符需要的操作数. 
更新公式: 
a, b, c 分别表示替换, 删除, 添加
1. 替换
dp[i-1][j-1] 到 dp[i][j] 表示需要两个字符串各自加一位, 
那么, 如果word1[i] == word2[j]不需要替换, 则 a = dp[i-1][j-1], 
否则, a = dp[i-1][j-1] + 1 

2. 删除
dp[i-1][j] 到 dp[i][j] 表示word1前i-1个字符已经满足, 
那么, 只需要删除新加的字符就可以转换为word2前j个字符.
b = dp[i-1][j] + 1

3. 添加
dp[i][j-1] 到 dp[i][j] 表示word1前i-1个字符已经满足了word2前j-1个字符.
那么, 只需要对word1添加word2的第j个字符即可.
c = dp[i][j-1] + 1

最后, 
dp[i][j] = min([a, b, c])
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0] = i 
        for i in range(1, len(word2)+1):
            dp[0][i] = i 
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                b, c = dp[i-1][j] + 1, dp[i][j-1] + 1 
                if word1[i-1] == word2[j-1]:
                    a = dp[i-1][j-1]
                else:
                    a = dp[i-1][j-1] + 1 
                dp[i][j] = min([a, b, c])
        return dp[-1][-1]
