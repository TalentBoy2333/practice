public class LIS{
    public static void main(String[] args) {
        int nums[] = {10,9,2,5,3,7,101,18};
        for(int n: nums){
            System.out.print(n + " ");
        }
        System.out.println();

        int len = lengthOfLIS(nums);

        System.out.println("Longest Increasing Subsequence: " + len);
    }

    static int lengthOfLIS(int [] nums){
        if(nums == null || nums.length == 0) return 0;
        // dp[i]: nums[0:i+1]中的最长递增子序列
        int [] dp = new int[nums.length];
        int maxLength = 0;
        for(int i = 0; i < nums.length; i++){
            dp[i] = 1;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
            if(dp[i] > maxLength) maxLength = dp[i];
        }
        // for(int n: dp){
        //     System.out.print(n + " ");
        // }
        // System.out.println();
        return maxLength;
    }
}