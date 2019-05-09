/*
public class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}
*/
public class Solution {
    public RandomListNode Clone(RandomListNode pHead){
        // 注意: 不只要复制链表, 还要将原链表还原. 
        if(pHead == null){
            return null;
        }
        RandomListNode temp = pHead;
        while(temp != null){
            RandomListNode newNode = new RandomListNode(temp.label);
            newNode.next = temp.next;
            temp.next = newNode;
            temp = temp.next.next;
        }
        temp = pHead;
        while(temp != null){
            if(temp.random == null){
                temp.next.random = null;
            }else{
                temp.next.random = temp.random.next;
            }
            temp = temp.next.next;
        }
        RandomListNode copy = pHead.next;
        RandomListNode source = pHead;
        temp = copy;
        while(temp.next != null){
            source.next = temp.next;
            temp.next = temp.next.next;
            source = source.next;
            temp = temp.next;
        }
        source.next = null;
        return copy;
    }
}