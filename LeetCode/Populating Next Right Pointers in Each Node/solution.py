"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.p_list = list()
        self.part(root)
        return root
        
    def part(self, n):
        if n == None:
            return 0
        else:
            depth_left = self.part(n.left)
            depth_right = self.part(n.right)
            depth = max(depth_left, depth_right) + 1
            if depth > len(self.p_list):
                self.p_list.append(n)
            else:
                self.p_list[depth-1].next = n 
                self.p_list[depth-1] = n 
            return depth