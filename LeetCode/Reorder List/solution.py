# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s = []
        p = head 
        length = 0
        while p != None:
            s.append(p)
            p = p.next
            length += 1
        if length < 3:
            return
        p = head 
        while p != None and p != p.next:
            cur = s.pop()
            cur.next = p.next 
            p.next = cur 
            p = cur.next
        if p.next == p:
            p.next = None