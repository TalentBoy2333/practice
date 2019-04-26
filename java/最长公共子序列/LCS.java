public class LCS{
    public static void main(String[] args) {
        int s1[] = {1,3,4,5,6,7,7,8};
        int s2[] = {3,5,7,4,8,6,7,8,2};
        for(int n: s1) System.out.print(n);
        System.out.println();
        for(int n: s2) System.out.print(n);
        System.out.println();

        int lcs[] = getLCS(s1, s2);

        System.out.print("Longest Common Subsequence: ");
        for(int n: lcs) System.out.print(n + " ");
        System.out.println();
    }

    static int[] getLCS(int [] s1, int [] s2){
        int dp[][] = new int[s1.length+1][s2.length+1];
        for(int i = 1; i <= s1.length; i++){
            for(int j = 1; j <= s2.length; j++){
                if(s1[i-1] == s2[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
                else dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
        // for(int i = 0; i <= s1.length; i++){
        //     for(int j = 0; j <= s2.length; j++){
        //         System.out.print(dp[i][j] + "\t");
        //     }
        //     System.out.println();
        // }

        int i = s1.length;
        int j = s2.length;
        int index = dp[i][j];
        int lcs[] = new int[index];
        while(index > 0){
            if(i > 0 && dp[i][j] == dp[i-1][j]){
                i--;
            }else if(j > 0 && dp[i][j] == dp[i][j-1]){
                j--;
            }else{
                lcs[--index] = s1[i-1];
                i--;
                j--;
            }
        }
        return lcs;
    }
}