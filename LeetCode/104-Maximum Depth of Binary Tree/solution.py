# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_dep = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.part(root, 0)
        return self.max_dep
    
    def part(self, n, dep):
        if n == None:
            if dep > self.max_dep:
                self.max_dep = dep
            else:
                return
        else:
            self.part(n.left, dep+1)
            self.part(n.right, dep+1)