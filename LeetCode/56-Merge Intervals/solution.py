class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        l = sorted(intervals, key=lambda x:x[0])
        res = [] 
        ind = 0 
        # print(l)
        while ind < len(l):
            min_val = l[ind][0]
            max_val = l[ind][1]
            cur = ind + 1
            while cur < len(l) and max_val >= l[cur][0]:
                if l[cur][1] > max_val:
                    max_val = l[cur][1]
                cur += 1
            res.append([min_val, max_val])
            ind = cur
        return res

# so = Solution()
# res = so.merge([[1,3],[2,6],[8,10],[15,18]])
# print(res)