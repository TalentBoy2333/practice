public class Manacher{
    public static void main(String[] args) {
        String str = "aaaba";
        // String str = "saodfabcdcbakasf";
        System.out.println(str);
        char manacherCh[] = manacherString(str);
        System.out.print("Manacher String: ");
        for(char c: manacherCh) System.out.print(c + " ");
        System.out.println();

        int len[] = manacher(manacherCh);
        for(int i = 0; i < len.length; i++){
            if(manacherCh[i] != '#'){
                System.out.print((len[i]-1) + " ");
            }
        }
        System.out.println();
    }

    static char [] manacherString(String str){
        char ch[] = new char[2 * str.length() + 1];
        for(int i = 0; i < ch.length; i++){
            if(i % 2 == 0){
                ch[i] = '#';
            }else{
                ch[i] = str.charAt(i/2);
            }
        }
        return ch;
    }

    static int[] manacher(char [] ch){
        // 参考: https://www.cnblogs.com/z360/p/6375514.html
        int len[] = new int[ch.length];
        len[0] = 1;
        int po = 0;
        int p = 0;
        for(int i = 1; i < ch.length; i++){
            if(i <= p){
                int j = 2 * po - i;
                if(len[j] < p-i){
                    len[i] = len[j];
                }else{
                    int l = p - i + 1;
                    int low = i - l;
                    int high = i + l;
                    while(low >= 0 && high < ch.length && ch[low] == ch[high]){
                        low--;
                        high++;
                        l++;
                    }
                    len[i] = l;
                }
            }else{
                int l = 1;
                int low = i - 1;
                int high = i + 1;
                while(low >= 0 && high < ch.length && ch[low] == ch[high]){
                    low--;
                    high++;
                    l++;
                }
                len[i] = l;
            }
            if(len[i] + i - 1 > p){
                p = len[i] + i - 1;
                po = i;
            }
        }
        return len;
    }
}