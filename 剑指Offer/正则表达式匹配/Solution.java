public class Solution {
    public boolean match(char[] str, char[] pattern){
        return part(str, pattern, 0, 0);
    }
    
    private boolean part(char [] str, char [] pattern, int indStr, int indPat){
        if(indPat == pattern.length && indStr < str.length) return false;
        if(indPat == pattern.length && indStr == str.length) return true;
        if(indPat+1 < pattern.length && pattern[indPat+1] == '*'){
            if(indStr < str.length && (pattern[indPat] == '.' || pattern[indPat] == str[indStr])){
                return part(str, pattern, indStr, indPat+2) 
                    || part(str, pattern, indStr+1, indPat+2)
                    || part(str, pattern, indStr+1, indPat);
            }else{
                return part(str, pattern, indStr, indPat+2);
            }
        }else if(indStr < str.length && (pattern[indPat] == '.' || pattern[indPat] == str[indStr])){
            return part(str, pattern, indStr+1, indPat+1);
        }else{
            return false;
        }
    }
}