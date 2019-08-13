class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pre = 0 
        end = len(height) - 1
        res = 0
        while pre < end:
            area = (end - pre) * min(height[pre], height[end])
            if res < area:
                res = area
            if height[pre] > height[end]:
                end -= 1
            else:
                pre += 1
        return res 

# if __name__ == '__main__':
#     h = [1,8,6,2,5,4,8,3,7]
#     so = Solution() 
#     res = so.maxArea(h)
#     print(res)