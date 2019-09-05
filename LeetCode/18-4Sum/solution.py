class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        a = 0 
        b = len(nums) - 1 
        res = [] 
        for length in range(3, len(nums)):
            a = 0
            b = a + length
            while b < len(nums):
                c = a + 1 
                d = b - 1 
                while c < d:
                    cur = nums[a] + nums[b] + nums[c] + nums[d]
                    if cur > target:
                        d -= 1
                    elif cur < target:
                        c += 1
                    else:
                        if [nums[a], nums[b], nums[c], nums[d]] not in res:
                            res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                a += 1
                b += 1
        return res
            