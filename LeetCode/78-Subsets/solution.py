class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        length = len(nums)
        res = [[]]
        q = []
        for n in nums:
            q.append([n])
        res += q 
        while q != []:
            new_q = []
            # print(q)
            for l in q:
                ind = nums.index(l[-1])
                if ind >= length - 1:
                    continue 
                else:
                    for i in range(ind+1, length):
                        temp = l[:] + [nums[i]]
                        new_q.append(temp)
            res += new_q 
            q = new_q
        return res 

# if __name__ == '__main__':
#     so = Solution()
#     res = so.subsets([1,2,3])
#     print(res)