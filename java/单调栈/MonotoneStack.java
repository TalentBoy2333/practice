import java.util.Stack;

public class MonotoneStack{
    // 单调栈: 找到每一个元素左/右边第一个比它大/小的元素
    public static void main(String[] args) {
        int nums[] = {3,4,5,1,2};

        int res[] = leftSmall(nums);
        for(int n: res){
            System.out.print(n + " ");
        }
        System.out.println();
    }

    static int [] leftSmall(int [] nums){
        // 参考: https://blog.csdn.net/wubaizhe/article/details/70136174
        Stack<Integer> s = new Stack<>();
        int res[] = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            if(s.empty()){
                res[i] = -1;
            }else{
                while(!s.empty() && nums[s.peek()] >= nums[i]){
                    s.pop();
                }
                if(s.empty()){
                    res[i] = -1;
                }else{
                    res[i] = s.peek();
                }
            }
            s.push(i);
            System.out.println(s);
        }
        return res;
    }
}