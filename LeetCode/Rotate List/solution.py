# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        length = 0
        n = head 
        while n != None:
            length += 1
            n  = n.next
        move = k % length 
        if move == 0:
            return head
        new_head = head 
        for _ in range(length - move):
            new_head = new_head.next 
        if new_head == head:
            return head 

        n = new_head
        while n.next != None:
            n = n.next
        n.next = head 
        
        n = head 
        while n.next != new_head:
            n = n.next 
        n.next = None
        return new_head
