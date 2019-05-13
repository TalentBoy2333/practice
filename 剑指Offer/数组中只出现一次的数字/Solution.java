//num1,num2分别为长度为1的数组。传出参数
//将num1[0],num2[0]设置为返回结果
public class Solution {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        // 参考: https://github.com/ZXZxin/ZXBlog/blob/master/%E5%88%B7%E9%A2%98/Other/%E5%89%91%E6%8C%87Offer/%E5%89%91%E6%8C%87Offer%20-%2040%20-%20%E6%95%B0%E7%BB%84%E4%B8%AD%E5%8F%AA%E5%87%BA%E7%8E%B0%E4%B8%80%E6%AC%A1%E7%9A%84%E6%95%B0%E5%AD%97.md
        int allXor = 0;
        for(int n: array) allXor ^= n;
        int index = 0;
        while((allXor & (1<<index)) == 0) index++;
        for(int n: array){
            if((n & (1<<index)) == 0){
                num1[0] ^= n;
            }else{
                num2[0] ^= n;
            }
        }
    }
}