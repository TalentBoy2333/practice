# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False 
        return self.part(root, sum, 0)
        

    def part(self, n, sum, cur_sum):
        cur_sum += n.val 
        if n.left == None and n.right == None:
            if cur_sum == sum:
                return True
            else:
                return False
        else:
            if n.left == None:
                return self.part(n.right, sum, cur_sum)
            elif n.right == None:
                return self.part(n.left, sum, cur_sum)
            else:
                return self.part(n.left, sum, cur_sum) or self.part(n.right, sum, cur_sum)