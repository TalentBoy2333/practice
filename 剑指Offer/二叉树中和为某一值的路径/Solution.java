import java.util.ArrayList;
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
    ArrayList<ArrayList<Integer>> list = new ArrayList<>();
    public ArrayList<ArrayList<Integer>> FindPath(TreeNode root,int target) {
        if(root == null){
            return this.list;
        }
        ArrayList<Integer> p = new ArrayList<>();
        part(root, target, 0, p);
        return this.list;
    }

    private void part(TreeNode n, int target, int sum, ArrayList<Integer> p){
        if(n == null){
            return;
        }else{
            ArrayList<Integer> path = new ArrayList<>();
            for(int m: p){
                path.add(m);
            }
            path.add(n.val);
            sum += n.val;
            part(n.left, target, sum, path);
            part(n.right, target, sum, path);
            if(n.left == null && n.right == null && sum == target){
                this.list.add(path);
            }
        }
    }
}