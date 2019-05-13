public class Solution {
    public String LeftRotateString(String str,int n) {
        if("".equals(str)){
            return "";
        }
        int ind = n % str.length();
        String right = str.substring(0, ind);
        String left = str.substring(ind);
        return left + right;
    }
}