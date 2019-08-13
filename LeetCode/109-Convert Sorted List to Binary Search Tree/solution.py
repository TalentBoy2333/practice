# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        n = head 
        self.vals = list()
        while n != None:
            self.vals.append(n.val)
            n = n.next 
        self.ind = 0

        root = TreeNode(1)
        self.build_tree(root)
        self.part(root)
        return root

        
    def build_tree(self, n):
        pos = n.val 
        if 2*pos <= len(self.vals):
            n.left = TreeNode(2*pos)
            self.build_tree(n.left)
        if 2*pos+1 <= len(self.vals):
            n.right = TreeNode(2*pos+1)
            self.build_tree(n.right)

    def part(self, n):
        if n == None:
            return 
        else:
            self.part(n.left)
            n.val = self.vals[self.ind]
            self.ind += 1
            self.part(n.right)