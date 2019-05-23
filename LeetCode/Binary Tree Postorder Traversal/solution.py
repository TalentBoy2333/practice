# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        s1 = [root]
        s2 = []
        while s1 != []:
            cur = s1.pop()
            s2.append(cur.val)
            if cur.left != None:
                s1.append(cur.left)
            if cur.right != None:
                s1.append(cur.right)

        res = []
        while s2 != []:
            res.append(s2.pop())
        return res