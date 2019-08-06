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
            return None
        if head.next == None:
            return head
        pre = ListNode(0)
        pre.next = head
        n1 = pre 
        n2 = head
        n3 = head.next
        while n3 != None:
            if n2.val == n3.val:
                n2 = self.find_diff(n2, n3)
                n1.next = n2 
                n3 = n2.next if n2 != None else None
            else:
                n1 = n2 
                n2 = n3 
                n3 = n3.next
        return pre.next
            
        

    def find_diff(self, n1, n2):
        while n2 != None:
            if n2.val != n1.val:
                return n2 
            n2 = n2.next 
        return None