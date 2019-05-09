/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if(pHead1 == null || pHead2 == null){
            return null;
        }
        ListNode temp1 = pHead1, temp2 = pHead2;
        while(true){
            if(temp1 == temp2) return temp1;
            temp1 = temp1.next;
            temp2 = temp2.next;
            if(temp1 == null && temp2 == null) return null;
            if(temp1 == null) temp1 = pHead2;
            if(temp2 == null) temp2 = pHead1;
        }
    }
}