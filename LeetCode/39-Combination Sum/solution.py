class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = [] 
        self.part(candidates, target, [], 0)
        return self.res    

    def part(self, candidates, target, cur, index):
        if sum(cur) > target:
            return 
        elif sum(cur) == target:
            self.res.append(cur[:])
        else:
            for i in range(index, len(candidates)):
                n = candidates[i]
                new_cur = cur[:]
                new_cur.append(n)
                self.part(candidates, target, new_cur, i)