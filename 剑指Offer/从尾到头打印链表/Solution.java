/**
*    public class ListNode {
*        int val;
*        ListNode next = null;
*
*        ListNode(int val) {
*            this.val = val;
*        }
*    }
*
*/
import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
        ArrayList<Integer> list = new ArrayList<>();
        part(listNode, list);
        return list;
    }

    private void part(ListNode n, ArrayList<Integer> l){
        if(n == null){
            return;
        }else{
            part(n.next, l);
            l.add(n.val);
        }
    }
}