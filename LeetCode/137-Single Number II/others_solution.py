class Solution:
# @param A, a list of integer
# @return an integer
def singleNumber(self, A):
    ans = 0
    for i in xrange(0,32):
        count = 0
        for a in A:
            if ((a >> i) & 1):
                count+=1
        ans |= ((count%3) << i)
    return self.convert(ans)
    
def convert(self,x):
    if x >= 2**31:
        x -= 2**32
    return x