# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p1 = head
        p2 = head.next
        while p2 != None:
            pnext = p2.next # 保存next地址
            if p2.val <= head.val:
                p1.next = pnext
                p2.next = head
                head = p2
            elif p2.val >= p1.val:
                p1 = p2
            else:
                p1.next = pnext
                tp = head
                while tp != p1:
                    if tp.val <= p2.val and tp.next.val >= p2.val:
                        p2.next = tp.next
                        tp.next = p2
                        break
                    tp = tp.next
            p2 = pnext
        return head

