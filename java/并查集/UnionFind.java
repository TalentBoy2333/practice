// import java.io.BufferedInputStream;
import java.util.Scanner;

public class UnionFind{
    /* 
    * 题意就是告诉你0号同学被感染了, 他还参加了一些社团, 给出一些社团以及里面的人, 问总共多少人感染. 
    * 输入给出n表示人数(标号为0~n-1), m表示社团数目, 接下来m行每行第一个数k, 表示该社团有k人, 
    * 然后是k个人的编号. 要你输出有多少个人感染了病毒. 
    * 链接: http://poj.org/problem?id=1611
    */
    static int[] f; // f[i] 表示i节点的父节点
    static int[] rank; // rank[i] 以i节点为根节点的树的高度

    static int findRoot(int p){
        while(f[p] != p){
            f[p] = f[f[p]];
            p = f[p];
        }
        return p;
    }

    static void union(int a, int b){
        int aR = findRoot(a);
        int bR = findRoot(b);
        if(rank[aR] > rank[bR]){
            f[bR] = f[aR];
        }else if(rank[aR] < rank[bR]){
            f[aR] = f[bR];
        }else{
            f[aR] = f[bR];
            rank[aR]++;
        }
    }

    public static void main(String[] args) { 
        // Scanner in = new Scanner(new BufferedInputStream(System.in));
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            int n = in.nextInt(); // n个人
            int m = in.nextInt(); // m个社团
            System.out.println("m: " + m + "\t n: " + n);
            if(m == 0 && n == 0) break;
            f = new int[n];
            rank = new int[n];
            for(int i = 0; i < n; i++){
                f[i] = i;
                rank[i] = 1;
            }
            for(int i = 0; i < m; i++){
                int num = in.nextInt(); // 该社团的人数
                int root = in.nextInt(); // 该社团第一个人的编号
                for(int j = 0; j < num-1; j++){
                    int p = in.nextInt(); // 该社团剩余的人的编号
                    union(root, p);
                }
            }
            int res = 1; // 已知0号已经感染
            int root0 = findRoot(0);
            for(int i = 1; i < n; i++){
                if(findRoot(i) == root0){
                    res++;
                }
            }
            System.out.println("SARS People number: " + res);
        }
    }
}