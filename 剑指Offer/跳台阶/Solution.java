public class Solution {
    public int JumpFloor(int target) {
        return Fibonacci(target+1);
    }

    private int Fibonacci(int n) {
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }
        int a = 0; 
        int b = 1;
        for(int i = 2; i <= n; i++){
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}