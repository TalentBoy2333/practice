class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                b = s.pop()
                a = s.pop()
                print(a, b)
                if c == "+":
                    s.append(int(a + b))
                elif c == "-":
                    s.append(int(a - b))
                elif c == "*":
                    s.append(int(a * b))
                else:
                    s.append(int(a / b))
            else:
                s.append(int(c))
        return s[0]

if __name__ == '__main__':
    a = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    s = Solution()
    n = s.evalRPN(a)
    print(n)