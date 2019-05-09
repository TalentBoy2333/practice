public class Solution {
    public int GetNumberOfK(int [] array , int k) {
       int low = firstEqual(array, k);
       int high = lastEqual(array, k);
    //    System.out.println(low);
    //    System.out.println(high);
       if(low == -1) return 0;
       else return high - low + 1;
    }

    private int firstEqual(int [] array, int k){
        int low = 0; 
        int high = array.length - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(array[mid] >= k) high = mid - 1;
            else low = mid + 1;
        }
        if(low < array.length && array[low] == k) return low;
        else return -1;
    }
    private int lastEqual(int [] array, int k){
        int low = 0; 
        int high = array.length - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(array[mid] > k) high = mid - 1;
            else low = mid + 1;
        }
        if(high >= 0 && array[high] == k) return high;
        else return -1;
    }
}