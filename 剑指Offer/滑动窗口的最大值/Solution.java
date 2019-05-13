import java.util.ArrayList;
import java.util.LinkedList;

public class Solution {
    public ArrayList<Integer> maxInWindows(int [] num, int size){
        ArrayList<Integer> list = new ArrayList<>();
        if(num.length < size || size <= 0){
            return list;
        }
        LinkedList<Integer> q = new LinkedList<>();
        for(int i = 0; i < num.length; i++){
            if(i >= size && !q.isEmpty() && (i-size) == q.peek()) q.poll();
            while(!q.isEmpty() && num[q.peekLast()] < num[i]){
                q.pollLast();
            }
            q.add(i);
            // System.out.println(q);
            if(i >= size-1) list.add(num[q.peek()]);
        }
        return list;
    }
}