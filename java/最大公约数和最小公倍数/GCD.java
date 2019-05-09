public class GCD{
    public static void main(String[] args) {
        int a = 21;
        int b = 14;
        int gcd = calGCD(a, b);
        System.out.println("GCD of " + a + " and " + b + ": " + gcd);
    }

    static int calGCD(int a, int b){
        // 参考: https://blog.csdn.net/only_invarably/article/details/64967860
        int r;
        int max = Math.max(a, b);
        int min = Math.min(a, b);
        while(min != 0){
            r = max % min;
            max = min;
            min = r;
        }
        return max;
    }
}