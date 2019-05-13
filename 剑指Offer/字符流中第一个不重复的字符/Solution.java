public class Solution {
    // 参考: https://github.com/ZXZxin/ZXBlog/blob/master/%E5%88%B7%E9%A2%98/Other/%E5%89%91%E6%8C%87Offer/%E5%89%91%E6%8C%87Offer%20-%2054%20-%20%E5%AD%97%E7%AC%A6%E6%B5%81%E4%B8%AD%E7%AC%AC%E4%B8%80%E4%B8%AA%E4%B8%8D%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%97%E7%AC%A6.md
    int hash[] = new int[256];
    int ind = 1;
    //Insert one char from stringstream
    public void Insert(char ch){
        if(hash[ch] == 0){
            hash[ch] = ind++;
        }else{
            hash[ch] = -1;
        }
    }
  //return the first appearence once char in current stringstream
    public char FirstAppearingOnce(){
        int minInd = Integer.MAX_VALUE;
        char res = '#';
        for(int i = 0; i < hash.length; i++){
            if(hash[i] > 0 && hash[i] < minInd){
                minInd = hash[i];
                res = (char)i;
            }
        }
        return res;
    }
}