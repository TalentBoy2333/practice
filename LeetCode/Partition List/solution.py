# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        super_pre = ListNode(0)
        super_pre.next = head 
        n = head 
        while n != None and n.val < x:
            n = n.next
        if n == None or n.next == None:
            return head
        else:
            mid = n 

        n1 = super_pre
        n2 = head
        flag = False
        while n2 != None:
            if n2 == mid:
                flag = True
            if n2.val < x and flag:
                n1.next = n2.next 
                self.insert(super_pre, n2, mid)
                n2 = n1.next
            else:
                n1 = n1.next 
                n2 = n2.next
        return super_pre.next


    def insert(self, super_pre, n, mid):
        n1 = super_pre 
        n2 = super_pre.next 
        while n2 != mid:
            n1 = n1.next 
            n2 = n2.next
        n1.next = n 
        n.next = n2