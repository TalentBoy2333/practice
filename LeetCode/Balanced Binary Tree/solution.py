# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = True 

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.part(root)
        return self.res
        
    def part(self, n):
        if n == None:
            return 0
        else:
            dep_left = self.part(n.left)
            dep_right = self.part(n.right)
            if abs(dep_left - dep_right) > 1:
                self.res = False
            return max(dep_left, dep_right) + 1