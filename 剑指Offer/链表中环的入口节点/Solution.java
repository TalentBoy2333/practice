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

    public ListNode EntryNodeOfLoop(ListNode pHead){
        if(pHead == null) return null;
        if(pHead.next == null) return null;
        ListNode p1 = pHead;
        ListNode p2 = pHead.next;

        ListNode p = findOne(p1, p2);
        if(p == null) return null;
        int len = calLen(p);
        p1 = pHead;
        p2 = p1;
        for(int i = 0; i < len; i++){
            p2 = p2.next;
        }
        return findEntry(p1, p2);
    }

    private ListNode findOne(ListNode p1, ListNode p2){
        while(p1 != null && p2 != null){
            if(p1 == p2){
                return p1;
            }
            p1 = p1.next;
            if(p2.next == null) return null;
            p2 = p2.next.next;
        }
        return null;
    }

    private int calLen(ListNode p){
        ListNode temp = p.next;;
        int len = 1;
        while(temp != p){
            len++;
            temp = temp.next;
        }
        return len;
    }

    private ListNode findEntry(ListNode p1, ListNode p2){
        while(p1 != p2){
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}