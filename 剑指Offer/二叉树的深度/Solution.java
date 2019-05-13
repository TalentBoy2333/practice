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
    public int TreeDepth(TreeNode root) {
        return part(root, 0);
    }

    public int part(TreeNode n, int depth){
        if(n == null){
            return depth;
        }else{
            int left = part(n.left, depth+1);
            int right = part(n.right, depth+1);
            return Math.max(left, right);
        }
    }
}