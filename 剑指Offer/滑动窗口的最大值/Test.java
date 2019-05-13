import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Test{
    public static void main(String[] args) {
        int num[] = {2,3,4,2,6,2,5,1};
        for(int n: num) System.out.print(n + " ");
        System.out.println();
        Solution s = new Solution();
        ArrayList<Integer> l = s.maxInWindows(num, 3);
        System.out.println(l);
    }
}