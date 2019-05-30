class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = []
        number = len(ratings)
        """
        遍历两边，首先每个人得一块糖，第一遍从左到右，若当前点比前一个点高就比前者多一块。
        这样保证了在一个方向上满足了要求。第二遍从右往左，若左右两点，左侧高于右侧，但
        左侧的糖果数不多于右侧，则左侧糖果数等于右侧糖果数+1，这就保证了另一个方向上满足要求
        """
        for _ in range(number): # 初始将每个孩子的糖果数都设为1
            candy.append(1)
        for i in range(1, number):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        for i in range(number-2, -1, -1):
            if ratings[i] > ratings[i+1] and candy[i] <= candy[i+1]:
                candy[i] = candy[i+1] + 1
        # print(candy)
        return sum(candy)

# s = Solution()
# s.candy([1,3,4,5,2])
