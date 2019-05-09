public class Solution {
    public String replaceSpace(StringBuffer str) {
        int length = 0;
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == ' ') length += 3;
            else length++;
        }
        int low = str.length() - 1;
        str.setLength(length);
        int high = str.length() - 1;
        while(low >= 0){
            if(str.charAt(low) == ' '){
                str.setCharAt(high--, '0');
                str.setCharAt(high--, '2');
                str.setCharAt(high--, '%');
            }else{
                str.setCharAt(high--, str.charAt(low));
            }
            low--;
        }
        return str.toString();
    }
}