class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        step = 0
        while cur < len(nums)-1:
            print(cur)
            max_val = 0
            max_ind = 0
            for i in range(1, nums[cur]+1):
                if cur+i >= len(nums)-1:
                    return step+1
                if nums[cur+i]+i > max_val:
                    max_val = nums[cur+i]+i
                    max_ind = cur+i 
            cur = max_ind 
            step += 1
        return step

# so = Solution()
# res = so.jump([4,1,1,3,1,1,1])
# print(res)