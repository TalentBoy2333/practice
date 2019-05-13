public class Solution {
    public boolean isContinuous(int [] numbers) {
        if(numbers.length == 0){
            return false;
        }
        int hash[] = new int[14];
        int max = 0;
        int min = 14;
        int count = 0;
        for(int n: numbers){
            if(n == 0){
                count++;
            }else{
                if(n > max) max = n;
                if(n < min) min = n;
                if(hash[n] == 1) return false;
                else hash[n] = 1;
            }
        }
        if(count == 4){
            return true;
        }else if(max - min < 5){
            return true;
        }else{
            return false;
        }   
    }
}