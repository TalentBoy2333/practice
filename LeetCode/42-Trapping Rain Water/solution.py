class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.res = 0 
        self.part(height, 0, len(height)-1)
        return self.res 

    def part(self, nums, start, end):
        # print(start, end)
        if end - start > 1:
            max1_val = -1
            max1_ind = 0
            max2_val = -1
            max2_ind = 0
            for i in range(start, end+1):
                if nums[i] > max2_val:
                    max2_val = nums[i]
                    max2_ind = i 
                    if max2_val > max1_val:
                        max1_val, max2_val = max2_val, max1_val
                        max1_ind, max2_ind = max2_ind, max1_ind 
            if max2_ind < max1_ind:
                max1_val, max2_val = max2_val, max1_val
                max1_ind, max2_ind = max2_ind, max1_ind 
            max_h = min(max1_val, max2_val)
            rain = 0
            for i in range(max1_ind+1, max2_ind):
                rain = rain + (max_h - nums[i])
            self.res += rain
            self.part(nums, start, max1_ind)
            self.part(nums, max2_ind, end)
                

# so = Solution()
# res = so.trap([5,4,1,2])
# print(res)