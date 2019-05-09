/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode Merge(ListNode list1,ListNode list2) {
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        ListNode p1 = list1, p2 = list2;
        ListNode head = null;
        if(p1.val < p2.val){
            head = p1;
            p1 = p1.next;
        }else{
            head = p2;
            p2 = p2.next;
        } 
        ListNode temp = head;
        while(p1 != null && p2 != null){
            if(p1.val < p2.val){
                temp.next = p1;
                p1 = p1.next;
            }else{
                temp.next = p2;
                p2 = p2.next;
            } 
            temp = temp.next;
        }
        if(p1 == null){
            temp.next = p2;
        }else{
            temp.next = p1;
        }
        return head;
    }
}