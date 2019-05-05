public class BigMultiply{
    public static void main(String[] args) {
        String str1 = "31452650798";
        String str2 = "41598746521";
        System.out.println(str1);
        System.out.println(str2);

        String result = bigMultiplyd(str1, str2);
        System.out.println(str1 + " * " + str2 + " = " + result);
    }

    static String bigMultiplyd(String str1, String str2){
        int n1[] = new int[str1.length()];
        int n2[] = new int[str2.length()];
        int n[] = new int[str1.length() + str2.length()];
        // 翻转字符串中的数字
        for(int i = 0; i < n1.length; i++){
            n1[i] = str1.charAt(n1.length - 1 - i) - '0';
        } 
        for(int i = 0; i < n2.length; i++){
            n2[i] = str2.charAt(n2.length - 1 - i) - '0';
        }
        // 乘法竖式规律
        for(int i = 0; i < str1.length(); i++){
            for(int j = 0; j < str2.length(); j++){
                n[i+j] += n1[i] * n2[j];
            }
        }
        for(int i = 0; i < n.length - 1; i++){
            if(n[i] > 9){
                n[i+1] += n[i] / 10;
                n[i] = n[i] % 10;
            }
        }
        StringBuilder result = new StringBuilder();
        int i;
        // 找到最高位位置
        for(i = n.length - 1; i >= 0; i--) if(n[i] != 0) break;
        // 由于一开始翻转数组, 所以这里要从后向前加入到结果中
        for(; i >= 0; i--){
            result.append(n[i]);
        }
        return result.toString();
    }
}

