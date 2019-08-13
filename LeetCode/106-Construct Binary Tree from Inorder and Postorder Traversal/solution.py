# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        root = self.part(inorder, postorder, 0, len(postorder)-1, 0)
        return root
        
    def part(self, inorder, postorder, post_a, post_b, in_a):
        root = TreeNode(postorder[post_b])
        in_mid = inorder.index(postorder[post_b])
        if in_mid - in_a > 0:
            new_post_b = in_mid - 1 - in_a + post_a
            root.left = self.part(inorder, postorder, post_a, new_post_b, in_a)
        else:
            root.left = None
        if (in_mid - in_a) < (post_b - post_a):
            new_post_a = in_mid - in_a + post_a 
            new_post_b = post_b - 1
            root.right = self.part(inorder, postorder, new_post_a, new_post_b, in_mid+1)
        else:
            root.right = None
        return root
            