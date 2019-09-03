class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        hsh = [0 for _ in range(length)]
        # print(hsh)
        for n in nums:
            if 0 <= n-1 < length:
                hsh[n-1] = 1
        for i in range(length):
            if hsh[i] == 0:
                return i + 1
        return length + 1