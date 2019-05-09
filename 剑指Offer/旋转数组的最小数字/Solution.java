import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if(array.length == 0){
            return 0;
        }
        return part(array, 0, array.length-1);
    }

    private int part(int [] array, int low, int high){
        if(low == high){
            return array[low];
        }
        if(high - low == 1){
            return Math.min(array[low], array[high]);
        }
        int mid = (low + high) / 2;
        if(array[low] <= array[mid] || array[mid] > array[high]){
            return part(array, mid, high);
        }else{
            return part(array, low, mid);
        }
    }
}