class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        length = len(prices)
        l_r = [0 for _ in range(length)]
        min_p = prices[0]
        for i in range(1, length):
            l_r[i] = max(prices[i] - min_p, l_r[i-1])
            min_p = min(min_p, prices[i])
        r_l = [0 for _ in range(length)]
        max_p = prices[-1]
        for i in range(length-2, -1, -1):
            r_l[i] = max(max_p - prices[i], r_l[i+1])
            max_p = max(max_p, prices[i])
        # print(l_r)
        # print(r_l)

        res = 0
        for i in range(length-1):
            res = max(res, l_r[i] + r_l[i+1], l_r[i])
        res = max(res, l_r[length-1])
        return res


        

# if __name__ == '__main__':
#     p = [3,3,5,0,0,3,1,4]
#     # p = [1,2,3,4,5]
#     print(p)
#     so = Solution()
#     res = so.maxProfit(p)
#     print(res)