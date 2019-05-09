/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode reConstructBinaryTree(int [] pre,int [] in) {
        return part(pre, in, 0, 0, pre.length-1);
    }

    private TreeNode part(int [] pre, int [] in, int preLow, int inLow, int len){
        TreeNode n = new TreeNode(pre[preLow]);
        int mid;
        for(mid = inLow; mid <= inLow + len; mid++){
            if(in[mid] == pre[preLow]) break;
        }
        if(mid > inLow){
            n.left = part(pre, in, preLow+1, inLow, mid-1-inLow);
        }else{
            n.left = null;
        }
        if(mid < inLow + len){
            n.right = part(pre, in, preLow+mid-inLow+1, mid+1, inLow+len-mid-1);
        }else{
            n.right = null;
        }
        return n;
    }
}