'''
动态规划
dp[i][j]表示s1的前 i 个字符, 和s2前 j 个字符能不能表示s3的前 i+j 个字符
因此, dp[i][j]公式为:
1. 如果, dp[i-1][j] == 0 and dp[i][j-1] == 0
   则, dp[i][j] = 0
2. 如果, dp[i-1][j] == 1 and s1[i] == s3[i+j]
   则, dp[i][j] = 1
   否则, dp[i][j] = 0
3. 如果, dp[i][j-1] == 1 and s2[j] == s3[i+j]
   则, dp[i][j] = 1
   否则, dp[i][j] = 0
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1) + 1
        l2 = len(s2) + 1
        l3 = len(s3)
        if l1 + l2 - 2 != l3:
            return False
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        dp[0][0] = 1
        for i in range(1, l1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = 1
            else:
                break
        for i in range(1, l2):
            if s2[i-1] == s3[i-1]:
                dp[0][i] = 1
            else:
                break
        for i in range(1, l1):
            for j in range(1, l2):
                if dp[i-1][j] == 0 and dp[i][j-1] == 0:
                    dp[i][j] = 0
                elif dp[i-1][j] == 1 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = 1
                elif dp[i][j-1] == 1 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        # for l in dp:
        #     print(l)
        if dp[l1-1][l2-1] == 0:
            return False
        else:
            return True

# if __name__ == '__main__':
#     so = Solution()
#     s1 = "aabcc"
#     s2 = "dbbca"
#     s3 = "aadbbcbcac"
#     res = so.isInterleave(s1, s2, s3)
#     print(res)