class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.res = []
        flag = [0 for _ in range(len(nums))]
        self.part(nums, 0, [], flag)
        return self.res
        

    def part(self, nums, index, cur, flag):
        # print(index, cur)
        if index == len(nums):
            self.res.append(cur[:])
        else:
            new_flag = flag[:]
            new_cur = cur[:]
            self.part(nums, index+1, new_cur, new_flag)
            if index == 0 or nums[index] != nums[index-1] or (nums[index] == nums[index-1] and flag[index-1] == 1):
                new_cur.append(nums[index])
                new_flag[index] = 1
                self.part(nums, index+1, new_cur, new_flag)

# nums = [1,1,2,2]
# so = Solution() 
# res = so.subsetsWithDup(nums)
# print(res)