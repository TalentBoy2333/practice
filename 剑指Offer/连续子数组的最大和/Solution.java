public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        if(array.length == 0){
            return 0;
        }
        int sum = 0;
        int max = -99999;
        for(int n: array){
            if(sum <= 0){
                sum = 0;
            }
            sum += n;
            if(sum > max){
                max = sum;
            }
        }
        return max;
    }
}