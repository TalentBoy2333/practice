import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int x[] = new int[n];
        for(int i = 0; i < n; i++){
            x[i] = in.nextInt();
        }
        String res = solution(x);
        System.out.println(res);
    }

    static String solution(int [] x){
        if(x.length <= 2) return "Possible";
        Arrays.sort(x);
        int sub = x[1] - x[0];
        for(int i = 2; i < x.length; i++){
            if(x[i] - x[i-1] != sub){
                return "Impossible";
            }
        }
        return "Possible";
    }
}