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
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if(root1 == null || root2 == null){
            return false;
        }else{
            return part(root1, root2) || HasSubtree(root1.left, root2) || HasSubtree(root1.right, root2);
        }
    }

    private boolean part(TreeNode n1, TreeNode n2){
        if(n2 == null){
            return true;
        }else if(n1 == null){
            return false;
        }else{
            if(n1.val == n2.val){
                return part(n1.left, n2.left) && part(n1.right, n2.right);
            }else{
                return false;
            }
        }
    }
}