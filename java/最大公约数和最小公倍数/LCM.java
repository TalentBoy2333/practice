public class LCM{
    public static void main(String[] args) {
        int a = 12; 
        int b = 16;
        int lcm = calLCM(a, b);
        System.out.println("LCM of " + a + " and " + b + ": " + lcm);
    }

    static int calLCM(int a, int b){
        return a * b / calGCD(a, b);
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