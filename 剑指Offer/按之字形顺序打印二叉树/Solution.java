import java.util.ArrayList;
import java.util.Stack;
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
    ArrayList<ArrayList<Integer>> list = new ArrayList<>();
    public ArrayList<ArrayList<Integer>> Print(TreeNode pRoot) {
        if(pRoot == null){
            return this.list;
        }
        Stack<TreeNode> s = new Stack<>();
        s.push(pRoot);
        int level = 1;
        while(!s.isEmpty()){
            s = part(s, level);
            level++;
        }
        return this.list;
    }

    private Stack<TreeNode> part(Stack<TreeNode> s, int level){
        ArrayList<Integer> row = new ArrayList<>();
        Stack<TreeNode> newS = new Stack<>();
        while(!s.isEmpty()){
            TreeNode cur = s.pop();
            row.add(cur.val);
            if(level % 2 == 1){
                if(cur.left != null) newS.push(cur.left);
                if(cur.right != null) newS.push(cur.right);
            }else{
                if(cur.right != null) newS.push(cur.right);
                if(cur.left != null) newS.push(cur.left);
            }
        }
        this.list.add(row);
        return newS;
    }
}