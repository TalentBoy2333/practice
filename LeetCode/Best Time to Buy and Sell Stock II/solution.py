class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        cur = prices[0]
        profit = 0
        for n in prices[1:]:
            if n <= cur:
                cur = n
            else:
                profit += (n - cur)
                cur = n
        return profit

# p = [7,6,4,3,1]
# so = Solution()
# res = so.maxProfit(p)
# print(res)
