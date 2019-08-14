class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        res = []
        nums = sorted(nums)
        i = 0
        while i < length:
            while i > 0 and i < length and nums[i] == nums[i-1]:
                i += 1
            l = i + 1
            r = length - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < length and nums[l] == nums[l-1]:
                        l += 1
                    while r >= 0 and r < length - 1 and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res

# if __name__ == '__main__':
#     n = [-1,0,1,2,-1,-4]
#     so = Solution()
#     res = so.threeSum(n)
#     print(res)
