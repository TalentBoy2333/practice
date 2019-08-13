class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = self.count(nums)
        # print(nums)
        # print(flag)
        bin_list = []
        self.add_all(bin_list, nums)
        # print(bin_list)
        for i in range(len(bin_list)):
            bin_list[i] %= 3
        # print(bin_list)
        res = 0
        ind = 0
        for n in bin_list:
            res += n * 2**ind 
            ind += 1
        # print(flag * res)
        return flag * res

    def count(self, nums):
        positive = 0
        negative = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negative += 1
                nums[i] *= -1
            else:
                positive += 1
        if positive % 3 == 0:
            return -1
        else:
            return 1

    def add_all(self, bin_list, nums):
        for num in nums:
            ind = 0
            while num != 0:
                b = num % 2
                try:
                    bin_list[ind] += b
                except:
                    bin_list.append(b)
                num = num // 2
                ind += 1
    
# if __name__ == '__main__':
#     nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
#     s = Solution()
#     s.singleNumber(nums)

