public class NQueen{
    public static void main(String[] args) {
        nQueen(4);
    }

    static void nQueen(int n){
        int queen[] = new int[n]; // 表示第i行的皇后位于第queue[i]列
        for(int i = 0; i < n; i++){
            queen[0] = i;
            nQueenPart(n, queen, 1);
        }
    }

    static void nQueenPart(int n, int [] queen, int row){
        if(row == n){
            System.out.println("One solution: ");
            for(int i = 0; i < n; i++){
                System.out.println(i + " " + queen[i]);
            }
        }else{
            for(int i = 0; i < n; i++){
                boolean flag = true;
                for(int j = 0; j < row; j++){
                    int x = queen[j], y = j;
                    if(x == i || (x+y) == (i+row) || (x-y) == (i-row)){
                        flag = false;
                    }
                }
                if(flag){
                    queen[row] = i;
                    nQueenPart(n, queen, row+1);
                }
            }
        }
    }
}