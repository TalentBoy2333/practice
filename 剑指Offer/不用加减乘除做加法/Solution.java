public class Solution {
    public int Add(int num1,int num2) {
        int upper = (num1 & num2) << 1;
        int add = num1 ^ num2;
        while(upper != 0){
            upper = (num1 & num2) << 1;
            add = num1 ^ num2;
            num1 = upper;
            num2 = add;
        }
        return add;
    }
}