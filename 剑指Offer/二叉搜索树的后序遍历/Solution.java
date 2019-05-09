public class Solution {
    public boolean VerifySquenceOfBST(int [] sequence) {
        if(sequence.length == 0){
            return false;
        }
        return part(sequence, 0, sequence.length-1);
    }

    private boolean part(int [] sequence, int low, int high){
        if(low >= high){
            return true;
        }
        int head = sequence[high];
        boolean flag = true; // true: 小, false: 大
        int mid = 0;
        for(int i = low; i < high; i++){
            if(!flag && sequence[i] < head){
                return false;
            }else if(flag && sequence[i] > head){
                mid = i;
                flag = false;
            }
        }
        return part(sequence, low, mid-1) && part(sequence, mid, high-1);
    }
}