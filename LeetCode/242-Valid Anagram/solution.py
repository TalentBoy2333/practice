class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hsh1 = [0 for _ in range(26)]
        hsh2 = [0 for _ in range(26)]
        for c in s:
            ci = ord(c) - ord('a')
            hsh1[ci] += 1
        for c in t:
            ci = ord(c) - ord('a')
            hsh2[ci] += 1
        if hsh1 == hsh2:
            return True 
        else:
            return False