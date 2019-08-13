class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num1 = 0
        num2 = 0
        num3 = 0
        for n in nums:
            if n == 0:
                num1 += 1
            elif n == 1:
                num2 += 1
            else:
                num3 += 1
        ind = 0
        for _ in range(num1):
            nums[ind] = 0
            ind += 1
        for _ in range(num2):
            nums[ind] = 1
            ind += 1
        for _ in range(num3):
            nums[ind] = 2
            ind += 1
        