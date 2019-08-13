# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head 
        p1 = pre 
        p2 = head 
        for _ in range(m-1):
            p1 = p1.next 
            p2 = p2.next
        mid = p2 
        # print(p1.val)
        # print(mid.val)
        if mid.next == None: 
            return head
        p1.next = None 
        pre_end = p1
        
        p1 = mid
        p2 = mid.next 
        for _ in range(n-m):
            p1 = p1.next
            p2 = p2.next
        # print(p1.val)
        # print(p2.val) 
        p1.next = None
        end = p2 

        p1 = mid 
        p2 = mid.next
        p3 = mid.next
        while p3 != None:
            p3 = p3.next
            p2.next = p1 
            p1 = p2
            p2 = p3 
            
        mid.next = end
        pre_end.next = p1
        return pre.next
        
# if __name__ == '__main__':
#     so = Solution()
#     head = ListNode(1)
#     temp = head 
#     temp.next = ListNode(2)
#     temp = temp.next
#     temp.next = ListNode(3)
#     temp = temp.next
#     temp.next = ListNode(4)
#     temp = temp.next
#     temp.next = ListNode(5)
#     temp = head 
#     while temp != None:
#         print(temp.val, end='  ')
#         temp = temp.next
#     print()
#     head = so.reverseBetween(head, 2, 4)
#     temp = head 
#     while temp != None:
#         print(temp.val, end='  ')
#         temp = temp.next
#     print()
            

