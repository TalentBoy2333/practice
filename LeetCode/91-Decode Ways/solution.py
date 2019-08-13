class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1 
        for i in range(1, len(s)):
            if int(s[i]) == 0 and (int(s[i-1]) == 0 or int(s[i-1]) > 2):
                return 0
            elif int(s[i]) == 0:
                dp[i] = dp[i-2] if (i-2 >= 0) else 1
            elif int(s[i-1]) > 2 or int(s[i-1]) == 0:
                dp[i] = dp[i-1]
            elif int(s[i-1]) == 2 and 7 <= int(s[i]) <= 9:
                dp[i] = dp[i-1]
            else:
                dp[i] = (dp[i-2] + dp[i-1]) if (i-2 >= 0) else 2
        # print(dp)
        return dp[-1]

# if __name__ == '__main__':
#     so = Solution()
#     s = "12"
#     res = so.numDecodings(s)
#     print(res)


