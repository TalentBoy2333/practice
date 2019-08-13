# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p1 = head 
        p2 = head.next 
        while p2 != None:
            if p1.val == p2.val:
                p1.next = p2.next 
                p2 = p2.next 
            else:
                p1 = p1.next 
                p2 = p2.next
        return head