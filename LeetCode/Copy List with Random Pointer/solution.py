"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        self.add(head)
        self.set_random(head)
        # show(head)
        new_head = head.next
        self.divide(head, new_head)
        return new_head

        
    def add(self, n):
        cur = n
        while cur != None:
            temp = Node(cur.val, cur.next, None)
            cur.next = temp 
            cur = cur.next.next

    def set_random(self, n):
        cur = n
        while cur != None:
            if cur.random == None:
                cur.next.random = None
            else:
                cur.next.random = cur.random.next
            cur = cur.next.next

    def divide(self, head, new_head):
        cur1, cur2 = head, new_head
        while cur2.next != None:
            cur1.next = cur2.next
            cur1 = cur1.next
            cur2.next = cur1.next
            cur2 = cur2.next
        cur1.next = None

# def show(n):
#     cur = n
#     while cur != None:
#         print(cur.val, '\t', end='')
#         if cur.next == None:
#             print('None\t', end='')
#         else:
#             print(cur.next.val, '\t', end='')
#         if cur.random == None:
#             print('None\t', end='')
#         else:
#             print(cur.random.val, '\t')
#         cur = cur.next
#     print()

# if __name__ == '__main__':
#     head = Node(1, None, None)
#     cur = head 
#     cur.next = Node(2, None, None)
#     cur.random = cur.next 
#     cur = cur.next 
#     cur.random = cur 
#     show(head)

#     s = Solution()
#     new_head = s.copyRandomList(head)
#     show(new_head)
#     show(head)