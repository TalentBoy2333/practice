import java.util.ArrayList;
import java.util.Queue;
import java.util.PriorityQueue;
import java.util.Collections;

public class Solution {
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        /*
        * 使用PriorityQueue当作Heap，每次返回最大的值。
        * Time complexity is O(nlogk) 
        */
        ArrayList<Integer> l = new ArrayList<>();
        if(input.length == 0 || input.length < k || k <= 0){
            return l;
        }
        Queue<Integer> queue = new PriorityQueue<>(k, Collections.reverseOrder());
        
        for(int i = 0; i < input.length; i++){
            if(i < k){
                queue.add(input[i]);
            }else{
                if(input[i] < queue.peek()){
                    queue.remove();
                    queue.add(input[i]);
                }
            }
        }
        while(!queue.isEmpty()){
            l.add(queue.remove());
        }
        return l;
    }
}