/**
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
    TreeNode head = null;
    TreeNode temp = null;
    public TreeNode Convert(TreeNode pRootOfTree) {
        part(pRootOfTree);
        return this.head;
    }

    private void part(TreeNode n){
        if(n == null){
            return;
        }else{
            part(n.left);
            if(head == null){
                this.head = n;
                this.temp = this.head;
            }else{
                n.left = this.temp;
                this.temp.right = n;
                this.temp = n;
            }
            part(n.right);
        }
    }
}