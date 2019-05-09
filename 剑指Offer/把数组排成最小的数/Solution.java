import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public String PrintMinNumber(int [] numbers) {
        String l[] = new String[numbers.length];
        for(int i = 0; i < numbers.length; i++){
            l[i] = String.valueOf(numbers[i]);
        }
        Arrays.sort(l, new Comparator<String>(){
            @Override
            public int compare(String a, String b){
                String s1 = a + b;
                String s2 = b + a;
                return s1.compareTo(s2);
            }
        });
        StringBuilder res = new StringBuilder();
        for(String str: l){
            res.append(str);
        }
        return res.toString();
    }
}