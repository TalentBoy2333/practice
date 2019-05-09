import java.util.ArrayList;
 
public class Solution {
    public boolean IsPopOrder(int [] pushA,int [] popA) {
        if(pushA.length == 0){
            return true;
        }
        if(pushA.length == 1){
            if(pushA[0] == popA[0]){
                return true;
            }else{
                return false;
            }
        }
        int flags[] = new int[popA.length];
        for(int i=1; i<popA.length; i++){
            if(!find(pushA, flags, popA[i-1], popA[i])){
                return false;
            }
        }
        return true;
    }
     
    public boolean find(int [] pushA, int [] flags, int pre, int num){
        int index = 0;
        for(int i=0; i<pushA.length; i++){
            if(pushA[i] == pre){
                flags[i] = 1;
                index = i;
                break;
            }
        }
        for(int i=index-1; i>=0; i--){
            if(flags[i] == 0){
                index = i;
                break;
            }
        }
        for(int i=index; i<pushA.length; i++){
            if(pushA[i] == num){
                return true;
            }
        }
        return false;
    }
}
