class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [] 
        self.part(nums, 0)
        return self.res
        
    def part(self, nums, index):
        if index == len(nums):
            self.res.append(nums[:])
        else:
            for i in range(index, len(nums)):
                if self.is_swap(nums, index, i):
                    self.swap(nums, index, i)
                    self.part(nums, index+1)
                    self.swap(nums, index, i)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def is_swap(self, nums, start, end):
        for i in range(start, end):
            if nums[i] == nums[end]:
                return False
        return True 

# so = Solution() 
# res = so.permuteUnique([1,2,2])
# print(res)