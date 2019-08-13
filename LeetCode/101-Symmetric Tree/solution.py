# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True 
        else:
            return self.part(root.left, root.right)

    def part(self, n1, n2):
        if n1 == None and n2 == None:
            return True 
        elif n1 != None and n2 == None:
            return False 
        elif n1 == None and n2 != None:
            return False
        else:
            if n1.val == n2.val:
                return self.part(n1.left, n2.right) and self.part(n1.right, n2.left)
            else:
                return False

        
   