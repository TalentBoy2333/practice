import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();
        int low = 1;
        int high = 2;
        while(low < (sum + 1) / 2){
            if(part(low, high) > sum){
                low++;
            }else if(part(low, high) < sum){
                high++;
            }else{
                ArrayList<Integer> temp = new ArrayList<>();
                for(int i = low; i <= high; i++){
                    temp.add(i);
                }
                list.add(temp);
                high++;
            }
        }
        return list;
    }
    private int part(int low, int high){
        int num = high - low + 1;
        int sum = (low + high) * num / 2;
        return sum;
    }
}