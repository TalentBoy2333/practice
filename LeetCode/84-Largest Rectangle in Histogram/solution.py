class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        res = 0
        s = [] 
        for i in range(len(heights)):
            # print(s)
            while s != [] and heights[s[-1]] > heights[i]:
                temp = s.pop()
                if (i - s[-1] -1) * heights[temp] > res:
                    res = (i - s[-1] -1) * heights[temp]
            s.append(i)
        return res

# if __name__ == '__main__':
#     so = Solution()
#     h = [2,1,5,6,2,3]
#     res = so.largestRectangleArea(h)
#     print(res)