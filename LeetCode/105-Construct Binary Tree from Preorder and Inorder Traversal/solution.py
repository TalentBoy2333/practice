# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        root = self.part(preorder, inorder, 0, len(preorder)-1, 0)
        return root
        

    def part(self, preorder, inorder, pre_a, pre_b, in_a):
        root = TreeNode(preorder[pre_a])
        in_mid = inorder.index(preorder[pre_a])
        if in_mid > in_a:
            new_pre_a = pre_a + 1
            new_pre_b = pre_a + in_mid - in_a
            root.left = self.part(preorder, inorder, new_pre_a, new_pre_b, in_a)
        else:
            root.left = None
        if (in_mid - in_a) < (pre_b - pre_a):
            new_pre_a = pre_a + in_mid - in_a + 1
            new_in_a = in_mid + 1
            root.right = self.part(preorder, inorder, new_pre_a, pre_b, new_in_a)
        else:
            root.right = None
        return root