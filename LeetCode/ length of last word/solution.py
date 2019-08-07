class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        s = s.rstrip()
        if s == '':
            return 0
        sl = s.split()
        return len(sl[-1])