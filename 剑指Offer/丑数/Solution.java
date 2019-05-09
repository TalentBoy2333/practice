import java.util.ArrayList;

public class Solution {
    int ind2 = 0;
    int ind3 = 0;
    int ind5 = 0;
    public int GetUglyNumber_Solution(int index) {
        if(index == 0){
            return 0;
        }
        ArrayList<Integer> ugly = new ArrayList<>();
        ugly.add(1);
        for(int i = 0; i < index-1; i++){
            int num2 = ugly.get(this.ind2) * 2;
            int num3 = ugly.get(this.ind3) * 3;
            int num5 = ugly.get(this.ind5) * 5;
            if(num2 <= num3 && num2 <= num5) ugly.add(num2);
            else if(num3 <= num2 && num3 <= num5) ugly.add(num3);
            else ugly.add(num5);
            updateInd(ugly);
        }
        return ugly.get(ugly.size()-1);
    }

    private void updateInd(ArrayList<Integer> l){
        int cur = l.get(l.size()-1);
        for(int i = this.ind2; i < l.size(); i++){
            if(l.get(i) * 2 > cur){
                this.ind2 = i;
                break;
            }
        }
        for(int i = this.ind3; i < l.size(); i++){
            if(l.get(i) * 3 > cur){
                this.ind3 = i;
                break;
            }
        }
        for(int i = this.ind5; i < l.size(); i++){
            if(l.get(i) * 5 > cur){
                this.ind5 = i;
                break;
            }
        }
    }

}