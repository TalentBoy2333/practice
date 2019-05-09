public class Test{
    public static void main(String[] args) {
        RandomListNode pHead = build();
        show(pHead);
    
        Solution s = new Solution();
        RandomListNode copy = s.Clone(pHead);
        System.out.println("pHead: ");
        show(pHead);
        System.out.println("Copy: ");
        show(copy);
    }

    static RandomListNode build(){
        RandomListNode pHead = new RandomListNode(1);
        RandomListNode temp = pHead;
        for(int i = 2; i <= 5; i++){
            temp.next = new RandomListNode(i);
            temp = temp.next;
        }
        temp = pHead;
        temp.random = pHead.next.next; // 1.random -> 3
        temp = temp.next;
        temp.random = pHead.next.next.next.next; // 2.random -> 5
        temp = temp.next;
        temp.random = null; // 3.random -> null
        temp = temp.next;
        temp.random = pHead.next; // 4.random -> 2
        temp = temp.next;
        temp.random = null; // 5.random -> null
        return pHead;
    }

    static void show(RandomListNode pHead){
        RandomListNode temp = pHead;
        while(temp != null){
            System.out.print(temp.label + "\t");
            temp = temp.next;
        }
        System.out.println();
        temp = pHead;
        while(temp != null){
            if(temp.random == null){
                System.out.print("#\t");
            }else{
                System.out.print(temp.random.label + "\t");
            }
            temp = temp.next;
        }
        System.out.println();
    }
}

class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}