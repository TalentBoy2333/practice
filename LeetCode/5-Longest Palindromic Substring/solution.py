class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.start = 0
        self.length = 0
        for i in range(len(s)-1):
            self.part(s, i, i)
            self.part(s, i, i+1)
        return s[self.start:self.start+self.length+1]
        
    def part(self, s, i, j):
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break 
        i += 1
        j -= 1
        if j - i > self.length:
            print(i, j)
            self.length  = j - i 
            self.start = i

# so = Solution()
# res = so.longestPalindrome('babad')
# print(res)