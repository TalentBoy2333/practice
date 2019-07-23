# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2 
        pre = ListNode(0)
        cur = pre 
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                cur.next = p1 
                p1 = p1.next 
            else:
                cur.next = p2 
                p2 = p2.next 
            cur = cur.next 
        if p1 != None:
            cur.next = p1 
        if p2 != None:
            cur.next = p2
        return pre.next