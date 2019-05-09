import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> printMatrix(int [][] matrix) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int top = 0;
        int bot = matrix.length-1;
        int left = 0;
        int right = matrix[0].length-1;
        int i = 0;
         
        while(top <= bot && left <= right){
            i = left;
            while(i <= right){
                list.add(matrix[top][i]);
                i++;
            }
            i = top+1;
            while(i <= bot){
                list.add(matrix[i][right]);
                i++;
            }
            if(top != bot){
                i = right-1;
                while(i >= left){
                    list.add(matrix[bot][i]);
                    i--;
                }
            }
            if(right != left){
                i = bot-1;
                while(i > top){
                    list.add(matrix[i][left]);
                    i--;
                }
            }
             
            top++;
            bot--;
            left++;
            right--;
        }
         
        return list;
    }
}