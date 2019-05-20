import java.util.ArrayList;
import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        int n = solution(s);
        System.out.println(n);
    }

    static int solution(String s){
        ArrayList<Character> l = new ArrayList<>();
        for(Character c: s.toCharArray()){
            if(!l.contains(c)){
                l.add(c);
            }
        }
        if(l.size() > 2){
            return 0;
        }else if(l.size() == 1){
            return 1;
        }else{
            return 2;
        }
    }
}