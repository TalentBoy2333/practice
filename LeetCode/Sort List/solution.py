# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def show(l):
    temp = l
    while temp != None:
        print(temp.val, '  ', end='')
        temp = temp.next
    print()

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge_sort(head)
        
    def find_mid(self, head):
        slow = head
        fast = head.next 
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next
        return slow

    def merge_sort(self, head):
        if head == None:
            return None
        if head.next == None:
            return head
        mid = self.find_mid(head)
        l1 = head 
        l2 = mid.next
        mid.next = None 
        l1 = self.merge_sort(l1)
        l2 = self.merge_sort(l2)
        # show(l1)
        # show(l2)
        head = self.merge(l1, l2)
        return head
    
    def merge(self, l1, l2):
        if l1 == None:
            return l2 
        if l2 == None:
            return l1 
        super_head = ListNode(0)
        l = super_head
        while l1 != None and l2 != None :
            if l1.val < l2.val:
                l.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l.next = ListNode(l2.val)
                l2 = l2.next
            l = l.next 
        if l1 == None:
            l.next = l2 
        if l2 == None:
            l.next = l1
        return super_head.next

if __name__ == '__main__':
    head = ListNode(4)
    temp = head 
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(1)
    temp = temp.next
    temp.next = ListNode(3)
    temp = head
    while temp is not None:
        print(temp.val, '  ', end='')
        temp = temp.next
    print()

    s = Solution()
    # print(s.find_mid(head).val)
    temp = s.sortList(head)
    while temp is not None:
        print(temp.val, '  ', end='')
        temp = temp.next
    print()