# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
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
        self.flag = 0
        while q != []:
            q = self.part(q)
        return self.res


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
        if self.flag % 2 == 0:
            self.res.append(res)
        else:
            self.res.append(res[::-1])
        self.flag += 1
        return new_q