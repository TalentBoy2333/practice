import java.util.ArrayList;

public class Test{
    public static void main(String[] args) {
        String str = "aa";
        Solution s = new Solution();
        ArrayList<String> l = s.Permutation(str);
        for(String st: l){
            System.out.println(st);
        }
    }
}