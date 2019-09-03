class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.part('', n, n)
        return self.res

    def part(self, cur, count_l, count_r):
        if count_l == 0 and count_r == 0:
            self.res.append(cur[:])
            return 
        if count_l == 0:
            new_cur = cur[:]
            for i in range(count_r):
                new_cur += ')'
            self.res.append(new_cur[:])
            return 
        if count_l == count_r:
            new_cur = cur[:] + '('
            self.part(new_cur, count_l-1, count_r)
        elif count_l < count_r:
            new_cur = cur[:] + '('
            self.part(new_cur, count_l-1, count_r)
            new_cur = cur[:] + ')'
            self.part(new_cur, count_l, count_r-1)
        else:
            return 