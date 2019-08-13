# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.min_depth = 999999

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.part(root, 1)
        return self.min_depth
        
    def part(self, n, depth):
        if (n.left is None) and (n.right is None):
            if depth < self.min_depth:
                self.min_depth = depth
        else:
            if n.left is not None:
                self.part(n.left, depth+1)
            if n.right is not None:
                self.part(n.right, depth+1)