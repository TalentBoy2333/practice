'''
设 n 阶格雷码集合为 G(n), 则 G(n+1) 阶格雷码为: 
给 G(n) 阶格雷码每个元素二进制形式前面添加 0, 得到 G'(n); 
设 G(n) 集合倒序(镜像)为 R(n), 给 R(n) 每个元素二进制形式前面添加 1, 得到 R'(n); 
G(n+1) = G'(n) U R'(n)
拼接两个集合即可得到下一阶格雷码。

链接：https://leetcode-cn.com/problems/two-sum/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/

'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        cur = [[0], [1]]
        for _ in range(2, n+1):
            new_gray = []
            for code in cur:
                new_gray.append([0] + code)
            for i in range(len(cur)-1, -1, -1):
                code = cur[i]
                new_gray.append([1] + code)
            cur = new_gray[:]
        res = []
        for l in cur:
            res.append(self.part(l))
        return res
    
    def part(self, l):
        s = [str(n) for n in l]
        s = ''.join(s)
        return int(s, 2)
            
        
    

# if __name__ == '__main__':
#     so = Solution()
#     res = so.grayCode(3)
#     print(res)
