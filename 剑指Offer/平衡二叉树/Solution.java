public class Solution {
    // 参考: https://github.com/ZXZxin/ZXBlog/blob/master/%E5%88%B7%E9%A2%98/Other/%E5%89%91%E6%8C%87Offer/%E5%89%91%E6%8C%87Offer%20-%2039%20-%20%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.md
    public boolean IsBalanced_Solution(TreeNode root) {
        return part(root) > -1;
    }

    public int part(TreeNode n){
        if(n == null){
            return 0;
        }else{
            int left = part(n.left);
            int right = part(n.right);
            if(Math.abs(left - right) >= 2 || left == -1 || right == -1){
                return -1;
            }else{
                return Math.max(left, right) + 1;
            }
        }
    }
}

