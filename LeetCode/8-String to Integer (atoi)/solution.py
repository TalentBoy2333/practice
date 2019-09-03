class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '' or not ('0' <= s[0] <= '9' or s[0] == '-' or s[0] == '+'):
            return 0
        if s[0] == '-':
            flag = -1
            start = 1
        elif s[0] == '+':
            flag = 1
            start = 1
        else:
            flag = 1 
            start = 0
        if start == len(s):
            return 0
        if not ('0' <= s[start] <= '9'):
            return 0

        s_num = ''
        i = start 
        while i < len(s) and '0' <= s[i] <= '9':
            s_num += s[i]
            i += 1
                
        '''
        INT_MAX (2^31 − 1) or INT_MIN (−2^31) 
        '''
        # print(flag, s_num)
        if s_num == '':
            return 0
        if flag == -1 and int(s_num) > 2**31:
            return -1 * 2**31
        if flag == 1 and int(s_num) > 2**31-1:
            return 2**31 - 1
        return flag * int(s_num)
        
# so = Solution()
# res = so.myAtoi('+-12')
# print(res)