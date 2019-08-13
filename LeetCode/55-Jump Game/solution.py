'''
如果我们可以从数组中的某个位置跳到最后的位置, 
就称这个位置是"好坐标", 否则称为"坏坐标". 
问题可以简化为第 0 个位置是不是"好坐标". 
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if max(nums) == 1 and min(nums) == 1:
            return True
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(0, i):
                if dp[j] and (i-j) <= nums[j]:
                    dp[i] = True
                    break
        # print(dp)
        return dp[-1]

# if __name__ == '__main__':
#     so = Solution() 
#     n = [3,2,1,0,4]
#     res = so.canJump(n)
#     print(res)
        