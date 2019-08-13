# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.cur = -9999999999
        self.flag = True
        self.mid_scan(root)
        return self.flag


    def mid_scan(self, n):
        if n == None:
            return 
        else:
            self.mid_scan(n.left)
            if n.val <= self.cur:
                self.flag = False
            self.cur = n.val 
            self.mid_scan(n.right)