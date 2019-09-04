class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        '''
        d = {'I':1, 'IV':-2, 'V':5, 'IX':-2, 'X':10, 'XL':-20, 'L':50, 'XC':-20, \
             'C':100, 'CD':-200, 'D':500, 'CM':-200, 'M':1000}
        cl = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        csl = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        res = 0
        for c in cl:
            res = res + d[c] * s.count(c)
        for c in csl:
            res = res + d[c] * s.count(c)
        return res

# so = Solution() 
# res = so.romanToInt('MCMXCIV')
# print(res)