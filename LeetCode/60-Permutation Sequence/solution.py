'''
n = 3,k = 3的时候
nums=[1,2,3]的数组全排列为

123
132 --- 1 * 2!
213
231 --- 2 * 2!
312
321 ----3 * 2!

循环：
如果(i-1)*(n - 1)! < k <= i * (n - 1)!
那个第一个数字就应该为nums[i - 1]
将这个数剔除nums中:nums.erase(nums.begin() + (i - 1));
k = k - (i - 1) * ( n - 1)!

作者：bu-gao-su-ni-4
链接：https://leetcode-cn.com/problems/permutation-sequence/solution/60-di-kge-pai-lie-by-bu-gao-su-ni-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        jie = [1, 1]
        for i in range(2, n+1):
            jie.append(jie[-1] * i)
        nums = [i for i in range(1, n+1)]
        res = []
        
        count = 0
        while nums != []:
            # print(nums)
            # print(res)
            # print()
            length = len(nums)
            for i in range(0, length):
                if i * jie[length-1] < k <= (i+1) * jie[length-1]:
                    k -= i * jie[length-1] 
                    res.append(nums.pop(i))
                    break
        sl = [str(i) for i in res]
        res = ''.join(sl)
        return res



# so = Solution()
# res = so.getPermutation(3, 5)
# print(res)