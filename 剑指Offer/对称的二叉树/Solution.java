/*
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
    boolean isSymmetrical(TreeNode pRoot){
        if(pRoot == null){
            return true;
        }else{
            return part(pRoot.left, pRoot.right);
        }
    }

    private boolean part(TreeNode n1, TreeNode n2){
        if(n1 == null && n2 == null){
            return true;
        }else if(n1 == null || n2 == null){
            return false;
        }else{
            if(n1.val != n2.val){
                return false;
            }else{
                return part(n1.left, n2.right) && part(n1.right, n2.left);
            }
        }
    }
}