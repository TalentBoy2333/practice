public class Solution {
    int count = 0;
    public int InversePairs(int [] array) {
        if(array.length == 0){
            return 0;
        }
        sort(array, 0, array.length-1);
        return this.count;
    }

    public void sort(int [] array, int low, int high){
        if(low >= high) return;
        int mid = (low + high) / 2;
        sort(array, low, mid);
        sort(array, mid+1, high);
        merge(array, low, mid, high);
    }
    public void merge(int [] array, int low, int mid, int high){
        int newArr[] = new int[array.length];
        int i = mid, j = high;
        int ind = high;
        while(i >= low && j > mid){
            if(array[i] > array[j]){
                newArr[ind--] = array[i--];
                this.count += (j - mid);
            }else{
                newArr[ind--] = array[j--];
            }
        }
        while(i >= low) newArr[ind--] = array[i--];
        while(j > mid) newArr[ind--] = array[j--];
        for(int k = low; k <= high; k++) array[k] = newArr[k];
    }
}