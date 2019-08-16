class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        j = len(nums) - 1
        while i < j:
            # print(i, j)
            while i < j and nums[j] == val:
                j -= 1
            while i < j and nums[i] != val:
                i += 1
            if i < j:
                self.swap(nums, i, j)
                i += 1
                j -= 1
        if nums[j] == val:
            return j
        else:
            return j + 1
        
    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]

# if __name__ == '__main__':
#     so = Solution()
#     res = so.removeElement([2],3)
#     print(res)