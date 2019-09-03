class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        point = 0 
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                point = i 
                break 
        # print(point)
        res1 = self.b_search(nums, 0, point-1, target)
        res2 = self.b_search(nums, point, len(nums)-1, target)
        return res1 or res2
        
    def b_search(self, nums, start, end, target):
        l = start
        r = end 
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return True 
        return False

# nums = [2,5,6,0,0,1,2]
# target = 0
# so = Solution()
# so.search(nums, target)