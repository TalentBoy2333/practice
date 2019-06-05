class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
        max_len = 0
        for k in d.keys():
            d[k] = 1
            cur_len = 1
            n = k + 1
            while (n in d) and (d[n] == 0):
                cur_len += 1
                d[n] = 1
                n += 1
            n = k - 1
            while (n in d) and (d[n] == 0):
                cur_len += 1
                d[n] = 1
                n -= 1
            if cur_len > max_len:
                max_len = cur_len 
        return max_len 

nums = [100, 4, 200, 1, 3, 2]
so = Solution()
res = so.longestConsecutive(nums)
print(res)
                