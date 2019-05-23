# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        p1 = head 
        p2 = head.next
        p = self.find_point(p1, p2)
        if p == None:
            return None
        length = self.cal_len(p)
        p1 = head
        p2 = head
        for _ in range(length):
            p2 = p2.next
        return self.find_first(p1, p2)
        
        
    def find_point(self, p1, p2):
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p2 != None:
                p2 = p2.next 
            if p1 == p2:
                return p1 
        return None # 无循环

    def cal_len(self, p):
        length = 1
        tp = p.next
        while tp != p:
            length += 1
            tp = tp.next
        return length

    def find_first(self, p1, p2):
        while p1 != p2:
            p1 = p1.next 
            p2 = p2.next
        return p1
