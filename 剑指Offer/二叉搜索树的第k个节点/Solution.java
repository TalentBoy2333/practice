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
import java.util.ArrayList;
public class Solution {
    ArrayList<TreeNode> list = new ArrayList<TreeNode>();
    TreeNode KthNode(TreeNode pRoot, int k){
        if(k <= 0){
            return null;
        }
        midScan(pRoot);
        if(k > list.size()){
            return null;
        }
        return list.get(k-1);
    }
     
    void midScan(TreeNode n){
        if(n != null){
            midScan(n.left);
            list.add(n);
            midScan(n.right);
        }
    }
}