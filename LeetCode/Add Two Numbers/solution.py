# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = l1, l2
        pre = ListNode(0)
        n = pre
        sup = 0
        while n1 != None or n2 != None:
            if n1 == None and n2 != None:
                num = n2.val + sup 
                n2 = n2.next 
            elif n1 != None and n2 == None:
                num = n1.val + sup 
                n1 = n1.next 
            else:
                num = n1.val + n2.val + sup 
                n1 = n1.next 
                n2 = n2.next 
            n.next = ListNode(num % 10)
            sup = num // 10
            n = n.next
        if sup == 1:
            n.next = ListNode(1)
        
        
        return pre.next
        

  