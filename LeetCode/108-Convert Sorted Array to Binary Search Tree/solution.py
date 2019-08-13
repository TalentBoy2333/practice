# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.ind = 0
        root = self.part(nums, 1)
        return root
        

    def part(self, nums, ind):
        if ind > len(nums):
            return None
        else:
            cur = TreeNode(0)
            cur.left = self.part(nums, 2*ind)
            cur.val = nums[self.ind]
            self.ind += 1
            cur.right = self.part(nums, 2*ind+1)
            return cur