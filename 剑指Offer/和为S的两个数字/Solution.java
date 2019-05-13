import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList<Integer> list = new ArrayList<>();
        if(array.length < 2){
            return list;
        }
        int low = 0, high = array.length-1;
        while(low <= high){
            if(array[low] + array[high] > sum) high--;
            else if(array[low] + array[high] < sum) low++;
            else break;
        }
        if(array[low] + array[high] == sum){
            list.add(array[low]);
            list.add(array[high]);
        }
        return list;
    }
}