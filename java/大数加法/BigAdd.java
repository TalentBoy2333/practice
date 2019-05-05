public class BigAdd{
    public static void main(String[] args) {
        String str1 = "31452650798";
        String str2 = "41598746521";
        System.out.println(str1);
        System.out.println(str2);

        String result = bigAdd(str1, str2);
        System.out.println(str1 + " + " + str2 + " = " + result);
    }

    static String bigAdd(String str1, String str2){
        int ind1 = str1.length() - 1;
        int ind2 = str2.length() - 1;
        String result = "";
        int upper = 0;
        while(ind1 >= 0 && ind2 >= 0){
            int n1 = Integer.valueOf(Character.toString(str1.charAt(ind1)));
            int n2 = Integer.valueOf(Character.toString(str2.charAt(ind2)));
            int n = n1 + n2 + upper;
            upper = n / 10;
            result = String.valueOf(n % 10) + result;
            ind1--;
            ind2--;
        }
        if(ind1 >= 0) result = str1.substring(0, ind1+1) + result;
        if(ind2 >= 0) result = str2.substring(0, ind2+1) + result;
        return result;
    }
}