# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        n1 = head 
        while n1!= None:
            length += 1
            n1 = n1.next
        ind = length - n
        pre = ListNode(0)
        pre.next = head 
        n1 = pre
        n2 = head 
        for i in range(ind):
            n1 = n1.next 
            n2 = n2.next 
        n1.next = n2.next 
        return pre.next