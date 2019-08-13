class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -99999
        cur = 0
        for n in nums:
            if cur + n < 0:
                cur = n 
            else:
                cur += n
            if cur > res:
                res = cur
            elif cur < 0:
                cur = 0
        return res

        