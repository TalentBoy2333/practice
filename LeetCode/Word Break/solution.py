class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False for _ in range(length+1)]
        dp[0] = True
        for pos in range(1, length+1):
            for i in range(0, pos):
                if dp[i] and s[i:pos] in wordDict:
                    dp[pos] = True
                    break
        # print(dp)
        return dp[length]

# string = "leetcode"
# wordDict = ["leet", "code"]
# s = Solution()
# res = s.wordBreak(string, wordDict)
# print(res)