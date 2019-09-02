class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        point = l 
        ind_l = self.b_search(nums, 0, point-1, target)
        ind_r = self.b_search(nums, point, len(nums)-1, target)
        if ind_l != -1:
            return ind_l 
        elif ind_r != -1:
            return ind_r 
        else:
            return -1

    def b_search(self, nums, i, j, target):
        l = i
        r = j 
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid 
        return -1
