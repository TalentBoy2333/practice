/*
 public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public ListNode deleteDuplication(ListNode pHead){
        if(pHead == null) return null;
        if(pHead.next == null) return pHead;
        ListNode head = new ListNode(0);
        head.next = pHead;
        ListNode pre = head;
        ListNode cur = pHead;
        ListNode next = pHead.next;
        while(next != null){
            if(cur.val == next.val){
                while(next != null && cur.val == next.val) next = next.next;
                pre.next = next;
                if(next == null) break;
                cur = pre.next;
                if(cur == null) break;
                else next = cur.next;
            }else{
                pre = pre.next;
                cur = cur.next;
                next = next.next;
            }
        }
        return head.next;
    }
}