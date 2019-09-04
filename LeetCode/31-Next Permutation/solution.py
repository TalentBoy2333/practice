'''
https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode/
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind = len(nums) - 1
        while ind > 0 and nums[ind] <= nums[ind-1]:
            ind -= 1
        if ind == 0:
            nums[:] = nums[::-1]
            return 
        i = ind - 1 
        j = ind 
        while j < len(nums) and nums[i] < nums[j]:
            j += 1
        nums[i], nums[j-1] = nums[j-1], nums[i]
        
        nums[ind:] = nums[ind:][::-1]
            

# so = Solution()
# nums = [3,2,1]
# so.nextPermutation(nums)
# print(nums)
