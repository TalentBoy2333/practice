public class Solution {
    public int NumberOf1Between1AndN_Solution(int n) {
        if(n == 0){
            return 0;
        }else if(n < 10){
            return 1;
        }
        int num = n;
        int wei = 0;
        while(num != 0){
            wei++;
            num /= 10;
        }
        int count = 0;
        // 1346~21345最高位, 21345(10000~19999), 12345(10000~12345)
        int highest = n / (int)Math.pow(10, wei-1);
        if(highest == 1){
            count += n % (int)Math.pow(10, wei-1) + 1;
        }else{
            count += (int)Math.pow(10, wei-1);
        }
        // 1346~21345后四位, 4位中每一位为1, 其他位都有1000种可能(000~999), 最后乘最高位
        count += (int)Math.pow(10, wei-2) * (wei - 1) * highest;
        // 0~1345中1的个数
        count += NumberOf1Between1AndN_Solution(n % (int)Math.pow(10, wei-1));
        return count;
    }
}