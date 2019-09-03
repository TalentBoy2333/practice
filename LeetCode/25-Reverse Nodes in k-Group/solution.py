# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0 
        n = head 
        while n != None:
            length += 1
            n = n.next    
        time = length // k 
        pre = ListNode(0)
        pre.next = head 
        n = pre 
        for _ in range(time):
            n = self.reverse(n, k)
        return pre.next

    def reverse(self, pre, k):
        head = pre.next 
        n = head
        for _ in range(k):
            n = n.next
        end = n 

        n1 = pre 
        n2 = head
        n3 = head.next 
        while n3 != end:
            n1 = n2 
            n2 = n3 
            n3 = n3.next 
            n2.next = n1 
        
        pre.next = n2 
        head.next = end
        return head

            

