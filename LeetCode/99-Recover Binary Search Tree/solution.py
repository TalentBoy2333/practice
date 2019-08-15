# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.l = []
        self.mid_scan(root)
        if len(self.l) < 2:
            return 
        diff = self.find(self.l)
        if len(diff) == 1:
            diff.append(diff[0]+1)
        self.ind = 0
        change = []
        self.find_diff(root, diff, change)
        change[0].val, change[1].val = change[1].val, change[0].val
        
    def mid_scan(self, n):
        if n == None:
            return
        else:
            self.mid_scan(n.left)
            self.l.append(n.val)
            self.mid_scan(n.right)

    def find(self, nums):
        diff = []
        length = len(nums)
        l, r = 1, length-2
        if nums[0] > nums[1]:
            diff.append(0)
            l = 0
        if nums[length-1] < nums[length-2]:
            diff.append(length-1)
            r = 0
        if len(diff) == 2:
            return diff 
        # print(l, r)
        while l < length-1 or r > 0:
            if l > 0:
                if nums[l] > nums[l-1] and nums[l] > nums[l+1]:
                    diff.append(l)
                    l = 0
                else:
                    l += 1
            if len(diff) == 2:
                break
            if r > 0:
                if nums[r] < nums[r-1] and nums[r] < nums[r+1]:
                    diff.append(r)
                    r = 0
                else:
                    r -= 1
            if len(diff) == 2:
                break
        return diff
    
    def find_diff(self, n, diff, change):
        if n == None:
            return 
        else:
            self.find_diff(n.left, diff, change)
            if self.ind in diff:
                change.append(n)
            self.ind += 1
            self.find_diff(n.right, diff, change)
            
# so = Solution()
# res = so.find([1,3,2])
# print(res)