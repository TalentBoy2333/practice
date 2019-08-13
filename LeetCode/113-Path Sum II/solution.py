# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.sum = sum 
        self.res = list()
        self.part(root, [], 0)
        return self.res
        

    def part(self, n, path, p_sum):
        if n == None:
            return 
        else:
            p_sum += n.val 
            cur_path = path[:]
            cur_path.append(n.val)
            if n.left == None and n.right == None and p_sum == self.sum:
                self.res.append(cur_path)
            else:
                self.part(n.left, cur_path, p_sum)
                self.part(n.right, cur_path, p_sum)
