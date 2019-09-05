class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        displayer = [[] for _ in range(numRows)]
        ind = 0
        while ind < len(s):
            i = 0 
            while ind < len(s) and i < numRows:
                displayer[i].append(s[ind])
                ind += 1
                i += 1
            i = numRows - 2 
            while ind < len(s) and i > 0:
                displayer[i].append(s[ind])
                ind += 1
                i -= 1
        res = [] 
        for l in displayer:
            for n in l:
                res.append(n)
        res = ''.join(res)
        return res

                