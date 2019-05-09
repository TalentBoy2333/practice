/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindKthToTail(ListNode head,int k) {
        int length = 0;
        ListNode temp = head;
        while(temp != null){
            length++;
            temp = temp.next;
        }
        if(k > length){
            return null;
        }
        temp = head;
        for(int i = 0; i < length - k; i++){
            temp = temp.next;
        }
        return temp;
    }
}