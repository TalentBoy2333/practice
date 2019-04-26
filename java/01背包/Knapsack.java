public class Knapsack{
    public static void main(String[] args) {
        // 背包问题: 给定一组物品，每种物品都有自己的重量和价格，在限定的总重量内，
        //          我们如何选择，才能使得物品的总价格最高。
        // w: 物品重量
        // v: 物品价值
        // n: 物品种类(编号0 ~ n-1)
        // c: 背包容量(0 ~ c)
        // m: 在装入第i种物品时，容量为j的背包能拥有的最大价值
        int w[] = {4,6,2,2,5,1}; 
        int v[] = {8,10,6,3,7,2};
        int n = w.length, c = 12;
        int m[][] = new int[n][c+1];

        dp(w, v, n, c, m);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < c+1; j++){
                System.out.print(m[i][j] + "\t");
            }
            System.out.println();
        }
    }

    static void dp(int [] w, int [] v, int n, int c, int [][] m){
        // 初始化m矩阵第一行
        for(int i = 0; i < c+1; i++){
            if(i < w[0]) m[0][i] = 0;
            else m[0][i] = v[0];
        }
        // 如果容量j小于物品重量w[i], 则无法装入, m[i][j]同上一行m[i-1][j]
        // 如果容量j大于等于物品重量w[i], 则可以装入，也可以不装入, 
        // 我们需要判断不装入时的价值m[i-1][j], 和装入时的价值m[i-1][j-w[i]] + v[i]的大小
        // m[i-1][j-w[i]]表示上一行中去掉物品i的重量所能获取的最大价值，为物品i腾出空间
        // 然后，加上v[i]表示上一行中为物品i腾出位置后的最大价值加上物品i的价值
        for(int i = 1; i < n; i++){
            for(int j = 0; j < c+1; j++){
                if(j < w[i]) m[i][j] = m[i-1][j];
                else m[i][j] = Math.max(m[i-1][j], m[i-1][j-w[i]] + v[i]);
            }
        }
    }
}