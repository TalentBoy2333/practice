class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] 
        front = ['(', '[', '{']
        back = [')', ']', '}']
        for c in s:
            if c in front:
                stack.append(c)
            else:
                if stack == []:
                    return False
                if back.index(c) == front.index(stack[-1]):
                    stack.pop()
                else:
                    return False 
        if stack == []:
            return True 
        else:
            return False
