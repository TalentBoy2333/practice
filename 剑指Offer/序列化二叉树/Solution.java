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
    StringBuilder treeStr = new StringBuilder();
    int strInd = 0;
    String Serialize(TreeNode root){
        if(root == null){
            this.treeStr.append("#,");
        }else{
            this.treeStr.append(String.valueOf(root.val));
            this.treeStr.append(",");
            Serialize(root.left);
            Serialize(root.right);
        }
        return this.treeStr.toString();
    }
    TreeNode Deserialize(String str){
        int high = this.strInd + 1;
        while(str.charAt(high) != ',') high++;
        String s = str.substring(this.strInd, high);
        this.strInd = high + 1;
        TreeNode n = null;
        if("#".equals(s)){
            return n;
        }else{
            int val = Integer.parseInt(s);
            n = new TreeNode(val);
            n.left = Deserialize(str);
            n.right = Deserialize(str);
        }
        return n;
    }
}