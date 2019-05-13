public class Solution {
    public boolean isNumeric(char[] str) {
        int index[] = new int[1];
        if(hasE(str, index)){
            // System.out.println("E:" + index[0]);
            if(index[0] == 0 || index[0] == str.length-1){
                return false;
            }
            return isNumber(str, 0, index[0]-1) && isNumberAfterE(str, index[0]+1, str.length-1);
        }else{
            return isNumber(str, 0, str.length-1);
        }
    }
     
    public boolean hasE(char [] str, int [] index){
        for(int i=0; i<str.length; i++){
            char c = str[i];
            if(c == 'e' || c == 'E'){
                index[0] = i;
                return true;
            }
        }
        return false;
    }
     
    public boolean isNumber(char [] str, int head, int end){
        boolean dot = false;
        int start = head;
        // System.out.println("head" + "\t" + "end");
        // System.out.println(head + "\t" + end);
        if(str[head] == '+' || str[head] == '-'){
            if(head+1 > end){
                return false;
            }
            if(!((str[head+1] >= '0' && str[head+1] <= '9') || (str[head+1] == '.'))){
                return false;
            }
            start = head + 1;
        }
        // System.out.println(start);
        if(str[end] == '.'){
            return false;
        }
        for(int i=start; i<=end; i++){
            if(!((str[i] >= '0' && str[i] <= '9') || (str[i] == '.'))){
                // System.out.println("Error 1");
                return false;
            }
            if(str[i] == '.' && dot){
                // System.out.println("Error 2");
                return false;
            }
            if(str[i] == '.' && !dot){
                dot = true;
            }
        }
        return true;
    }
 
    public boolean isNumberAfterE(char [] str, int head, int end){
        int start = head;
        // System.out.println("head" + "\t" + "end");
        // System.out.println(head + "\t" + end);
        if(str[head] == '+' || str[head] == '-'){
            if(head+1 > end){
                return false;
            }
            if(str[head+1] < '0' || str[head+1] > '9'){
                return false;
            }
            start = head + 1;
        }
        // System.out.println(start);
        for(int i=start; i<=end; i++){
            if(str[i] < '0' || str[i] > '9'){
                // System.out.println("Error 1");
                return false;
            }
        }
        return true;
    }
}