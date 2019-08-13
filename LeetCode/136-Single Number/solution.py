class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = nums[0]
        for i in range(1, len(nums)):
            single = single ^ nums[i]
        return single

if __name__ == '__main__':
    nums = [4,1,2,1,2,-4,-4]
    s = Solution()
    s.singleNumber(nums)