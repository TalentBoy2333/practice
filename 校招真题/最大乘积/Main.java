import java.util.Arrays;
import java.util.Scanner;
import java.util.Collections;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long a[] = new long[n];
        for(int i = 0; i < n; i++){
            a[i] = in.nextInt();
        }
        // for(int m: a){
        //     System.out.print(m + " ");
        // }
        // System.out.println();
        Long res = solution(a);
        System.out.println(res);
    }

    static long solution(long [] a){
        if(a.length < 3) return 0;
        final long minLong = Long.MIN_VALUE;
        final long maxLong = Long.MAX_VALUE;
        Long lMax[] = {minLong, minLong, minLong};
        Long lMin[] = {maxLong, maxLong};
        int count = 0;
        // for(int n: lMax) System.out.print(n + " ");
        // System.out.println();
        // for(int n: lMin) System.out.print(n + " ");
        for(long n: a){
            updateMax(n, lMax, count);
            updateMin(n, lMin, count);
            count++;
        }
        return Math.max(lMax[0] * lMax[1] * lMax[2], lMax[0] * lMin[0] * lMin[1]);
    }
    static void updateMax(long num, Long [] l, int count){
        if(count < 3){
            l[count] = num;
            Arrays.sort(l, Collections.reverseOrder());
        }else if(l[2] < num){
            l[2] = num;
            Arrays.sort(l, Collections.reverseOrder());
        }else{
            return;
        }
    }
    static void updateMin(long num, Long [] l, int count){
        if(count < 2){
            l[count] = num;
            Arrays.sort(l);
        }else if(l[1] > num){
            l[1] = num;
            Arrays.sort(l);
        }else{
            return;
        }
    }
}