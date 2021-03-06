import java.util.Stack;

public class Solution {
    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();
    
    public void push(int node) {
        s1.push(node);
        if(s2.isEmpty()){
            s2.push(node);
        }else if(node < s2.peek()){
            s2.push(node);
        }else{
            s2.push(s2.peek());
        }
    }
    
    public void pop() {
        s1.pop();
        s2.pop();
    }
    
    public int top() {
        return s1.peek();
    }
    
    public int min() {
        return s2.peek();
    }
}