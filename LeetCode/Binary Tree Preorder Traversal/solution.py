# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        res = []
        temp = root
        while temp != None or s != []:
            while temp != None:
                res.append(temp.val)
                s.append(temp)
                temp = temp.left 
            temp = s.pop().right
        return res
            