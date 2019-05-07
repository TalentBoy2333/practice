public class KMP{
    public static void main(String[] args) {
        String str1 = "abcababca";
        String str2 = "cab";

        int next[] = getNext(str1);
        for(int n: next) System.out.print(n + " ");
        System.out.println();
        
        int ind = kmp(str1, str2);
        System.out.println(ind);
    }

    static int [] getNext(String str){
        int next[] = new int[str.length() + 1];
        int i = 1, j = 0;
        next[1] = 0;
        while(i < str.length()){
            if(j == 0 || str.charAt(i-1) == str.charAt(j-1)){
                i++;
                j++;
                next[i] = j;
            }else{
                j = next[j];
            }
        }
        return next;
    }

    static int kmp(String str1, String str2){
        // str1为主串, str2为子串
        int i = 0;
        int j = 0;
        int next[] = getNext(str2);
        while(i < str1.length() && j < str2.length()){
            if(j == 0 || str1.charAt(i) == str2.charAt(j)){
                i++;
                j++;
            }else{
                j = next[j];
            }
        }
        if(j >= str2.length()){
            return i - str2.length();
        }else{
            return 0;
        }
    }
}