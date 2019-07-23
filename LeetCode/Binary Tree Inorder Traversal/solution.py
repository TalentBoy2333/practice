# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        s = list() 
        p = root 
        while s != [] or p != None:
            while p != None:
                s.append(p)
                p = p.left
            p = s.pop()
            res.append(p.val)
            p = p.right
        return res