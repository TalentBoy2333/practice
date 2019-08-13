# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        self.res = list()
        q = list()
        n = root 
        q.append(n)
        while q != []:
            q = self.part(q)
        return self.res[::-1]


    def part(self, q):
        new_q = list()
        res = list()
        while q != []:
            n = q.pop(0)
            res.append(n.val)
            if n.left != None:
                new_q.append(n.left)
            if n.right != None:
                new_q.append(n.right)
        self.res.append(res)
        return new_q