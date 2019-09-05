class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.part(s, p, 0, 0)

    def part(self, s, p, inds, indp):
        if inds == len(s) and indp == len(p):
            return True
        elif inds < len(s) and indp == len(p):
            return False 
        # print(inds, indp)
        if indp < len(p)-1 and p[indp+1] == '*':
            if inds < len(s) and (p[indp] == '.' or s[inds] == p[indp]):
                sit1 = self.part(s, p, inds, indp+2)
                sit2 = self.part(s, p, inds+1, indp+2)
                sit3 = self.part(s, p, inds+1, indp)
                return sit1 or sit2 or sit3 
            else:
                return self.part(s, p, inds, indp+2)
        if inds < len(s) and (p[indp] == '.' or s[inds] == p[indp]):
            return self.part(s, p, inds+1, indp+1)
        else:
            return False


# so = Solution()
# s = "aa"
# p = "a*c"
# res = so.isMatch(s, p)
# print(res)

'''
class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
'''