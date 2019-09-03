class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
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
        ge = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        shi = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        bai = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        qian = ['', 'M', 'MM', 'MMM']
        
        w1 = num % 10
        num = num // 10 
        w2 = num % 10 
        num = num // 10
        w3 = num % 10
        num = num // 10 
        w4 = num % 10 
        res = qian[w4] + bai[w3] + shi[w2] + ge[w1]
        return res 

# so = Solution() 
# res = so.intToRoman(1994)
# print(res)
