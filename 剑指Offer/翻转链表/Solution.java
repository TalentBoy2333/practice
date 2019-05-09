/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode temp1 = null;
        ListNode temp2 = head;
        ListNode temp3 = head;
        while(temp3 != null){
            temp3 = temp3.next;
            temp2.next = temp1;
            temp1 = temp2;
            temp2 = temp3;
        }
        return temp1;
    }
}