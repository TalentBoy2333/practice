public class Solution {
    public int MoreThanHalfNum_Solution(int [] array) {
        if(array.length == 0){
            return 0;
        }
        int count = 1;
        int num = array[0];
        for(int i = 1; i < array.length; i++){
            if(array[i] == num) count++;
            else count--; 
            if(count == 0){
                num = array[i];
                count = 1;
            }
        }
        count = 0;
        for(int n: array){
            if(n == num) count++;
        }
        if(count > array.length / 2) return num;
        else return 0;
    }
}