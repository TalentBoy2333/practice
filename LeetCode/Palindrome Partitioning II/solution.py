'''
解题思路: 动态规划问题
dp[i] - 表示子串（0，i）的最小回文切割，则最优解在dp[s.length-1]中。
分几种情况：
1.初始化：当字串s.substring(0,i+1)(包括i位置的字符)是回文时，dp[i] = 0(表示不需要分割)；否则，dp[i] = i（表示至多分割i次）;
2.对于任意大于1的i，如果s.substring(j,i+1)(j<=i,即遍历i之前的每个子串)是回文时，dp[i] = min(dp[i], dp[j-1]+1);
3.如果s.substring(j,i+1)(j<=i)不是回文时，dp[i] = min(dp[i],dp[j-1]+i+1-j);
'''
'''
祝那个一楼的兄弟早日分手.（https://www.nowcoder.com/questionTerminal/1025ffc2939547e39e8a38a955de1dd3）
'''
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.part(s)
        
    def is_palindrome(self, s):
        if s == s[::-1]:
            return True 
        else:
            return False 

    def part(self, s):
        dp = [0 for _ in range(len(s))]
        for i in range(len(dp)):
            if self.is_palindrome(s[:i+1]):
                continue
            dp[i] = i
            for j in range(1, i+1):
                if self.is_palindrome(s[j:i+1]):
                    dp[i] = min(dp[i], dp[j-1]+1)
                else:
                    dp[i] = min(dp[i], dp[j-1]+i-j+1)
        # print(dp)
        return dp[-1]

# s = 'daabce'
# so = Solution()
# res = so.minCut(s)
# print(res)