class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.part(s, 4, '')
        return self.res
        
    def part(self, s, wei, cur):
        if wei == 0 and s == '':
            self.res.append(cur[:-1])
            return 
        if len(s) == 0 or len(s) > wei * 3:
            return 

        new_cur = cur + s[:1] + '.'
        self.part(s[1:], wei-1, new_cur)

        if len(s) >= 2 and s[0] != '0':
            new_cur = cur + s[:2] + '.'
            self.part(s[2:], wei-1, new_cur)

        if len(s) >= 3 and int(s[:3]) <= 255 and s[0] != '0':
            new_cur = cur + s[:3] + '.'
            self.part(s[3:], wei-1, new_cur)

# so = Solution() 
# res = so.restoreIpAddresses("010010")
# print(res)