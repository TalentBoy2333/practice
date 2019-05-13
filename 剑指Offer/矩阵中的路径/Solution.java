public class Solution {
    public boolean hasPath(char[] matrix, int rows, int cols, char[] str){
        boolean flag[] = new boolean[rows*cols];
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(matrix[i*cols+j] == str[0]){
                    if(find(matrix, rows, cols, str, i, j, 0, flag)){
                        return true;
                    }
                    flag = new boolean[rows*cols];
                }
            }
        }
        return false;
    }
     
    public boolean find(char[] matrix, int rows, int cols, char[] str, int x, int y, int index, boolean [] flag){
        if(x < 0 || x >= rows || y < 0 || y >= cols){
            return false;
        }
        if(flag[x*cols+y]){
            return false;
        }
        // System.out.println(index + "\t" + x + "\t" + y + "\t" + matrix[x*cols+y]);
        if(matrix[x*cols+y] == str[index]){
            // for(int i=0; i<rows; i++){
            //     for(int j=0; j<cols; j++){
            //         System.out.print(flag[i*cols+j] + "\t");
            //     }
            //     System.out.println();
            // }
            // System.out.println();
            if(index == str.length-1){
                return true;
            }
            flag[x*cols+y] = true;
            boolean flag1 = find(matrix, rows, cols, str, x-1, y, index+1, flag);
            boolean flag2 = find(matrix, rows, cols, str, x+1, y, index+1, flag);
            boolean flag3 = find(matrix, rows, cols, str, x, y-1, index+1, flag);
            boolean flag4 = find(matrix, rows, cols, str, x, y+1, index+1, flag);
            if(flag1 || flag2 || flag3 || flag4){
                return true;
            }
        }
        return false;
    }
 
 
}
