import numpy as np 
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        length = len(points)
        if length == 0:
            return 0
        if length == 1:
            return 1
        res = 0
        for i in range(length-1):
            x, y = points[i]
            dup = 1 # 重合
            vcnt = 0 # 垂直
            k2num = dict()
            cur_max = 0
            for j in range(i+1, length):
                tx, ty = points[j]
                if tx == x and ty == y:
                    dup += 1
                elif tx == x:
                    vcnt += 1 
                    cur_max = max(cur_max, vcnt)
                else:
                    # case: [[0,0],[94911151,94911150],[94911152,94911151]]
                    # np.float128可以处理, 但是leetcode无法调用numpy..
                    k = np.float128(ty-y) / np.float128(tx-x) 
                    if k in k2num:
                        k2num[k] += 1
                    else:
                        k2num[k] = 1
                    cur_max = max(cur_max, k2num[k])
            res = max(res, cur_max+dup)
        return res

if __name__ == '__main__':
    # a = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    a = [[0,0],[94911151,94911150],[94911152,94911151]]
    s = Solution()
    res = s.maxPoints(a)
    print(res)