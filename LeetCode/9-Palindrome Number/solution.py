class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s_x = str(x)
        if s_x == s_x[::-1]:
            return True 
        else:
            return False