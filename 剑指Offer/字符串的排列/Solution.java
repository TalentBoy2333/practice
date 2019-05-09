import java.util.ArrayList;
public class Solution {
    // nowcoder不通过原因: 输出的全排列顺序不对。。。
    ArrayList<String> list = new ArrayList<>();
    public ArrayList<String> Permutation(String str) {
        if("".equals(str)){
            return this.list;
        }
        char chs[] = str.toCharArray();
        part(chs, 0);
        return this.list;
    }

    private void swap(char [] chs, int i, int j){
        char temp = chs[i];
        chs[i] = chs[j];
        chs[j] = temp;
    }
    private boolean isSwap(char [] chs, int low, int high){
        for(int i = low; i < high; i++){
            if(chs[i] == chs[high]){
                return false;
            }
        }
        return true;
    }
    private void part(char [] chs, int index){
        if(index == chs.length){
            String str = new String(chs);
            this.list.add(str);
        }
        
        for(int i = index; i < chs.length; i++){
            if(isSwap(chs, index, i)){
                swap(chs, index, i);
                part(chs, index+1);
                swap(chs, index, i);
            }
        }
    }
}