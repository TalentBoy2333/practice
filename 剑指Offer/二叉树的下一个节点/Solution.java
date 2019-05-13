/*
public class TreeLinkNode {
    int val;
    TreeLinkNode left = null;
    TreeLinkNode right = null;
    TreeLinkNode next = null;
 
    TreeLinkNode(int val) {
        this.val = val;
    }
}
*/
public class Solution {
    public TreeLinkNode GetNext(TreeLinkNode pNode)
    {
        if(pNode == null){
            return null;
        }
        if(pNode.right != null){
            return findRight(pNode.right);
        }else{
            if(pNode.next == null){
                return null;
            }
            if(pNode.next.left == pNode){
                return pNode.next;
            }
            if(pNode.next.right == pNode){
                return findLeftFather(pNode.next);
            }
        }
        return null;
    }
     
    public TreeLinkNode findRight(TreeLinkNode n){
        if(n.left == null){
            return n;
        }else{
            return findRight(n.left);
        }
    }
     
    public TreeLinkNode findLeftFather(TreeLinkNode n){
        if(n == null){
            return null;
        }else{
            if(n.next == null){
                return null;
            }else if(n.next.right == n){
                return findLeftFather(n.next);
            }else{
                return n.next;
            }
        }
    }
}