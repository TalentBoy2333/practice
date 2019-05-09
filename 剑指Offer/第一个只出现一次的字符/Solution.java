public class Solution {
    public int FirstNotRepeatingChar(String str) {
        if("".equals(str)){
            return -1;
        }
        int count[] = new int[52];
        int pos[] = new int[52];
        for(int i = 0; i < pos.length; i++) pos[i] = -1;
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(c >= 'a' && c <= 'z'){
                count[c-'a']++;
                if(pos[c-'a'] == -1) pos[c-'a'] = i;
            } 
            else{
                count[c-'A'+26]++;
                if(pos[c-'A'+26] == -1) pos[c-'A'+26] = i;
            }
        }
        int p = 100;
        for(int i = 0; i < count.length; i++){
            if(count[i] == 1 && pos[i] < p) p = pos[i];
        }
        if(p == 100){
            return -1;
        }else{
            return p;
        }
    }
}