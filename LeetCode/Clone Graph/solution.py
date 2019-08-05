"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        old = []
        new = []
        res = self.part(node, new, old)
        return res
    

    def part(self, node, new, old):
        if node in old:
            return new[old.index(node)]
        else:
            old.append(node)
            cur = Node(node.val, [])
            new.append(cur)
            for n in node.neighbors:
                cur.neighbors.append(self.part(n, new, old))
            return cur

        