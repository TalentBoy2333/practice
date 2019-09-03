class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # print(nums)
        length = len(nums)
        min_dis = 10**8
        min_val = 0
        for i in range(0, length-2):
            l = i+1
            r = length-1
            while l < r:
                if abs(nums[i] + nums[l] + nums[r] - target) < min_dis:
                    # print(nums[i], nums[l], nums[r])
                    min_dis = abs(nums[i] + nums[l] + nums[r] - target)
                    min_val = nums[i] + nums[l] + nums[r] 
                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    return target 
        return min_val

# so = Solution()
# res = so.threeSumClosest([-1, 2, 1, -4], 1)
# print(res)