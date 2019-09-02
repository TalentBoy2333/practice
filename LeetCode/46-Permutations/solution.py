class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.part(nums, 0)
        return self.res
        
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def part(self, cur, index):
        if index == len(cur):
            self.res.append(cur[:])
        else:
            for i in range(index, len(cur)):
                self.swap(cur, index, i)
                self.part(cur, index+1)
                self.swap(cur, index, i)

# so = Solution()
# res = so.permute([1,2,3])
# print(res)