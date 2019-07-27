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
        if root == None:
            return None
        l = list()
        l.append(root)
        while l != []:
            self.part2(l)
            l = self.part1(l)
            
        return root
        
    def part1(self, l):
        new_l = list()
        for n in l:
            if n.left != None:
                new_l.append(n.left)
            if n.right != None:
                new_l.append(n.right)
        return new_l 
    
    def part2(self, l):
        i = 0
        while i < len(l)-1:
            l[i].next = l[i+1]
            i += 1
        l[i].next = None 
        