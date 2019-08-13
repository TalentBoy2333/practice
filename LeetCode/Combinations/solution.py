class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.part([], n, k)
        return self.res

    def part(self, cur, n, k):
        if len(cur) == k:
            self.res.append(cur)
        else:
            if cur == []:
                end = 0
            else:
                end = cur[-1]
            for i in range(end+1, n+1):
                new_cur = cur[:]
                new_cur.append(i)
                self.part(new_cur, n, k)
    
# if __name__ == '__main__':
#     so = Solution()
#     res = so.combine(4, 2)
#     print(res)
