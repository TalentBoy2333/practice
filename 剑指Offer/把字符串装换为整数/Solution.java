public class Solution {
    public int StrToInt(String str) {
        if("".equals(str)) return 0;
        int flag = 1;
        if(str.charAt(0) == '+'){
            str = str.substring(1);
        }else if(str.charAt(0) == '-'){
            flag = -1;
            str = str.substring(1);
        }
        if("".equals(str)) return 0;
        int ind = 0;
        int num = 0;
        for(int i = str.length()-1; i >= 0; i--){
            if(str.charAt(i) >= '0' && str.charAt(i) <= '9'){
                int temp = str.charAt(i) - '0';
                num += temp * Math.pow(10, ind++) * flag;
            }else{
                return 0;
            }
        }
        return num;
    }
}