# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.part(root, 0)
        return self.sum
        
    def part(self, n, num):
        if n == None:
            return 
        else:
            num = num * 10 + n.val
            if n.left == None and n.right == None:
                self.sum += num
            else:
                self.part(n.left, num)
                self.part(n.right, num)