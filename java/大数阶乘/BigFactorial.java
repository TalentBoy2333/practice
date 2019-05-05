public class BigFactorial{
    public static void main(String[] args) {
        int n = 50;
        
        String result = bigFactorial(n);
        System.out.println(n + "! = " + result);
    }

    static String bigFactorial(int n){
        if(n < 0){
            return "";
        }else if(n == 0){
            return "1";
        }
        int res[] = new int[10000]; 
        res[0] = 1;
        int highInd = 0;
        for(int i = 2; i <= n; i++){
            // int num = 0;
            int upper = 0; // 进位
            int j;
            for(j = 0; j <= highInd || upper > 0; j++){
                // num += res[j] * i * Math.pow(10, j);
                int temp = res[j];
                res[j] = (temp * i + upper) % 10;
                upper = (temp * i + upper) / 10;
            }
            highInd = j - 1;
            // System.out.println(num);
            // for(int k = 0; k < 7; k++) System.out.print(res[k] + " ");
            // System.out.println();
        }
        StringBuilder result = new StringBuilder();
        int i;
        for(i = res.length - 1; i >= 0; i--) if(res[i] != 0) break;
        for(; i >= 0; i--){
            result.append(res[i]);
        }
        return result.toString();
    }
}