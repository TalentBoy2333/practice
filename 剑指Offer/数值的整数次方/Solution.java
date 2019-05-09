public class Solution {
    public double Power(double base, int exponent) {
        boolean flag = false;
        if(exponent < 0){
            flag = true;
            exponent = -1 * exponent;
        }
        if(flag){
            return 1 / part(base, exponent);
        }else{
            return part(base, exponent);
        }
    }

    private double part(double base, int exponent){
        if(exponent == 0){
            return 1;
        }
        if(exponent == 1){
            return base;
        }
        if(exponent % 2 == 1){
            return Power(base, exponent/2) * Power(base, exponent/2) * base;
        }else{
            return Power(base, exponent/2) * Power(base, exponent/2);
        }
    }
}