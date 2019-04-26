public class LCS{
    public static void main(String[] args) {
        String str1 = "acbcbcef";
        String str2 = "abcbced";

        String lcs = getLCS(str1, str2);
        
        System.out.println("Longest common substring: " + lcs);
    }

    static String getLCS(String s1, String s2){
        int dp[][] = new int[s1.length()+1][s2.length()+1];
        for(int i = 1; i <= s1.length(); i++){
            for(int j = 1; j <= s2.length(); j++){
                if(s1.charAt(i-1) == s2.charAt(j-1)) dp[i][j] = dp[i-1][j-1] + 1;
                else dp[i][j] = 0;
            }
        }

        int maxLength = 0;
        int x = 0, y = 0;
        for(int i = 0; i <= s1.length(); i++){
            for(int j = 0; j<= s2.length(); j++){
                System.out.print(dp[i][j] + "\t");
                if(dp[i][j] > maxLength){
                    maxLength = dp[i][j];
                    x = i-1;
                    y = j-1;
                }
            }
            System.out.println();
        }
        String lcs = "";
        while(maxLength > 0){
            lcs = Character.toString(s1.charAt(x--)) + lcs;
            maxLength--;
        }
        return lcs;
    }
}