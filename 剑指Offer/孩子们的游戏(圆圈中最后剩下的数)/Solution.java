import java.util.ArrayList;
public class Solution {
    public int LastRemaining_Solution(int n, int m) {
        if(n == 0){
            return -1;
        }
        int people = n;
        int index = 0;
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0; i<n; i++){
            list.add(i);
        }
        System.out.println(list);
        while(people > 1){
            index = (index+m-1) % people;
            list.remove(index);
            people--;
        }
        return list.get(0);
    }
}