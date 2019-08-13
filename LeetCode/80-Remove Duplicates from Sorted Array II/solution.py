class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        pre = 1
        end = 1
        cur = nums[0]
        flag = 1
        while end < len(nums):
            if nums[end] == cur:
                flag += 1
                if flag > 2:
                    end = self.find(nums, end)
                    flag = 1
            else:
                flag = 1
            if end == len(nums):
                return pre
            cur = nums[end]
            nums[pre] = nums[end]
            pre += 1
            end += 1
        return pre
    
    def find(self, nums, end):
        n = end + 1
        while n < len(nums):
            if nums[n] != nums[end]:
                return n
            n += 1
        return n
            
if __name__ == '__main__':
    n = [1,1,1]
    so = Solution()
    res = so.removeDuplicates(n)
    print(n[:res])