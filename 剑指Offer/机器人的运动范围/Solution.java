public class Solution {
    int number = 0;
    boolean flag[][] = null;
    public int movingCount(int threshold, int rows, int cols)
    {
        this.flag = new boolean[rows][cols];
        find(0, 0, rows, cols, threshold);
        return this.number;
    }
     
    public int calculate(int x, int y){
        int sum = 0;
        while(x > 0){
            sum += x % 10;
            x /= 10;
        }
        while(y > 0){
            sum += y % 10;
            y /= 10;
        }
        return sum;
    }
     
    public void find(int x, int y, int rows, int cols, int threshold){
        if(x >= rows || y >= cols || x < 0 || y < 0){
            return;
        }
        if(this.flag[x][y]){
            return;
        }
         
        if(calculate(x, y) <= threshold){
            this.number++;
            this.flag[x][y] = true;
            find(x-1, y, rows, cols, threshold);
            find(x+1, y, rows, cols, threshold);
            find(x, y-1, rows, cols, threshold);
            find(x, y+1, rows, cols, threshold);
        }else{
            this.flag[x][y] = true;
        }
    }
}