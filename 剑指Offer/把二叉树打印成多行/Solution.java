import java.util.ArrayList;
 
 
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
    ArrayList<ArrayList<Integer> > Print(TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
        if(pRoot == null){
            return list;
        }
        ArrayList<TreeNode> nodes = new ArrayList<TreeNode>();
        nodes.add(pRoot);
        while(!nodes.isEmpty()){
            nodes = part(nodes, list);
        }
        return list;
    }
     
    ArrayList<TreeNode> part(ArrayList<TreeNode> nodes, ArrayList<ArrayList<Integer>> list){
        ArrayList<TreeNode> newNodes = new ArrayList<TreeNode>();
        ArrayList<Integer> nodeVal = new ArrayList<Integer>();
        for(TreeNode temp: nodes){
            nodeVal.add(temp.val);
            if(temp.left != null){
                newNodes.add(temp.left);
            }
            if(temp.right != null){
                newNodes.add(temp.right);
            }
        }
        list.add(nodeVal);
        return newNodes;
    }
     
}