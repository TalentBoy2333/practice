# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = -99999
        self.part(root)
        return self.max_sum
        
    def part(self, n):
        if n == None:
            return 0
        else:
            left_sum = self.part(n.left)
            right_sum = self.part(n.right)
            path_sum = n.val + max(left_sum, 0) + max(right_sum, 0)
            if path_sum > self.max_sum:
                self.max_sum = path_sum
            path_sum = n.val + max(left_sum, right_sum, 0)
            return path_sum
