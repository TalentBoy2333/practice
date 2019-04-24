import java.util.Stack;

public class BLBinaryTree{
    public static void main(String[] args) {
        int arr[] = {-1,1,2,3,4,5,6,7};
        TreeNode head = buildTree(arr, 1);
        scan(head);
        System.out.println();

        preOrder(head);
        inOrder(head);
        postOrder(head);
    }

    static void scan(TreeNode n){
        if(n == null){
            System.out.print("# ");
        }else{
            System.out.print(n.val + " ");
            scan(n.left);
            scan(n.right);
        }
    }
    static TreeNode buildTree(int [] arr, int i){
        if(i >= arr.length || arr[i] == -1){
            return null;
        }else{
            TreeNode temp = new TreeNode(arr[i]);
            temp.left = buildTree(arr, 2*i);
            temp.right = buildTree(arr, 2*i+1);
            return temp;
        }
    }

    static void preOrder(TreeNode head){
        Stack<TreeNode> s = new Stack<>();
        TreeNode p = head;
        while(p != null || !s.isEmpty()){
            while(p != null){
                System.out.print(p.val + " ");
                s.push(p);
                p = p.left;
            }
            p = s.pop();
            p = p.right;
        }
        System.out.println();
    }

    static void inOrder(TreeNode head){
        Stack<TreeNode> s = new Stack<>();
        TreeNode p = head;
        while(p != null || !s.isEmpty()){
            while(p != null){
                s.push(p);
                p = p.left;
            }
            p = s.pop();
            System.out.print(p.val + " ");
            p = p.right;
        }
        System.out.println();
    }

    static void postOrder(TreeNode head){
        if(head == null) return;
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        s1.push(head);
        while(!s1.isEmpty()){
            TreeNode cur = s1.pop();
            s2.push(cur);
            if(cur.left != null) s1.push(cur.left);
            if(cur.right != null) s1.push(cur.right);
        }
        while(!s2.isEmpty()) System.out.print(s2.pop().val + " ");
        System.out.println();
    }
}