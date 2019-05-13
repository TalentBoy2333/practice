public class Solution {
    public int Sum_Solution(int n) {
        int num = 0;
        boolean temp = (n != 0) && (1 == (num = n + Sum_Solution(n-1)));
        return num;
    }
}