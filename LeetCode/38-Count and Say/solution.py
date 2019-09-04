class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        self.num_str = ['', '1']
        if n <= 1:
            return self.num_str[n]
        for i in range(2, n+1):
            # print(self.num_str[-1])
            self.part(self.num_str[-1])
        return self.num_str[-1]
        
    def part(self, s):
        cur = s[0]
        count = 0
        ind = 0
        res = ''
        while ind < len(s):
            while ind < len(s) and s[ind] == cur:
                ind += 1 
                count += 1
            res = res + str(count) + cur
            count = 0 
            if ind < len(s):
                cur = s[ind]
        # print(res)
        self.num_str.append(res)

# so = Solution() 
# so.countAndSay(10)