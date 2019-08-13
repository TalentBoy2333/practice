class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """        
        if rowIndex == 0:
            return [1]
        res = [1, 1]
        for i in range(2, rowIndex+1):
            cur = [0 for _ in range(i+1)]
            cur[0] = cur[-1] = 1
            for j in range(1, len(cur)-1):
                cur[j] = res[j-1] + res[j]
            res = cur
        return res