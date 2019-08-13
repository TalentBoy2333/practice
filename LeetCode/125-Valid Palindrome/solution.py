class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_list = list()
        for i in range(len(s)):
            if s[i] <= 'Z' and s[i] >= 'A':
                str_list.append(s[i].lower())
            elif (s[i] <= 'z' and s[i] >= 'a') or (s[i] <= '9' and s[i] >= '0'):
                str_list.append(s[i])
        # print(str_list)
        if str_list == str_list[::-1]:
            return True
        else:
            return False

# if __name__ == '__main__':
#     s = "0P"
#     so = Solution()
#     res = so.isPalindrome(s)
#     print(res)
