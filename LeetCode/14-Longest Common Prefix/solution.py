class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        res = ''
        length = 10**8
        for s in strs:
            if len(s) < length:
                length = len(s)
        for i in range(length):
            cur = strs[0][i]
            flag = True
            for s in strs:
                if s[i] != cur:
                    flag = False 
            if flag:
                res += cur 
            else:
                break 
        return res