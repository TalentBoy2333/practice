import java.util.Stack;

public class Solution {
    public String ReverseSentence(String str) {
        if("".equals(str)){
            return "";
        }
        Stack<String> s = new Stack<>();
        int low = 0;
        int high = 1;
        while(high < str.length()){
            if(str.charAt(high) == ' '){
                s.push(str.substring(low, high));
                low = high + 1;
                high = low + 1;
            }else{
                high++;
            }
        }
        s.push(str.substring(low));

        StringBuilder res = new StringBuilder();
        while(!s.isEmpty()){
            res.append(s.pop());
            res.append(" ");
        }
        return res.toString().substring(0, res.length()-1);
    }
}