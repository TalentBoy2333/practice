class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.part(s, [])
        return self.res
         
    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

    def part(self, s, l):
        if s == '':
            self.res.append(l)
        else:
            for i in range(1, len(s)+1):
                if self.is_palindrome(s[:i]):
                    temp = l[:]
                    temp.append(s[:i])
                    self.part(s[i:], temp)


# s = 'aab'
# so = Solution()
# res = so.partition(s)
# print(res)