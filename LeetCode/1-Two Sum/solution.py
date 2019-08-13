class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if(key in d.keys()):
                return d[key], i 
            else:
                d[nums[i]] = i
            # print(d)
        return 0, 0
        


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(nums)
    s = Solution()
    print(s.twoSum(nums, target))
