import java.util.LinkedList;
import java.util.Queue;

public class Dijkstra{
    public static void main(String[] args) {
        int graph[][] = {
            {0, 1, 5, 65535, 65535, 65535, 65535, 65535, 65535},
            {1, 0, 3, 7, 5, 65535, 65535, 65535, 65535},
            {5, 3, 0, 65535, 1, 7, 65535, 65535, 65535},
            {65535, 7, 65535, 0, 2, 65535, 3, 65535, 65535},
            {65535, 5, 1, 2, 0, 3, 6, 9, 65535},
            {65535, 65535, 7, 65535, 3, 0, 65535, 5, 65535},
            {65535, 65535, 65535, 3, 6, 65535, 0, 2, 7},
            {65535, 65535, 65535, 65535, 9, 5, 2, 0, 4},
            {65535, 65535, 65535, 65535, 65535, 65535, 7, 4, 0}
        };
        System.out.print("\t");
        for(int i = 0; i < graph.length; i++){
            System.out.print("v" + i + "\t");
        }
        System.out.println();
        for(int i = 0; i < graph.length; i++){
            System.out.print("v" + i + "\t");
            for(int j = 0; j < graph.length; j++){
                if(graph[i][j] == 65535) System.out.print("oo\t");
                else System.out.print(graph[i][j] + "\t");
            }
            System.out.println();
        }

        int minDis[] = dijkstra(graph, 0);
        for(int n: minDis) System.out.print(n + " ");
        System.out.println();
    }

    static int [] dijkstra(int [][] graph, int start){
        int minDis[] = new int[graph.length]; // start到i的最短距离
        int path[] = new int[graph.length]; // 前缀路径
        boolean flag[] = new boolean[graph.length];
        for(int i = 0; i < minDis.length; i++){
            minDis[i] = graph[start][i];
            flag[i] = true;
        }
        flag[start] = false;
        for(int p = 1; p < graph.length; p++){
            int min = 65535;
            int minInd = 0;
            for(int i = 0; i < minDis.length; i++){
                if(minDis[i] < min && flag[i]){
                    min = minDis[i];
                    minInd = i;
                }
            }
            flag[minInd] = false;
            for(int i = 0; i < graph.length; i++){
                if(minDis[minInd] + graph[minInd][i] < minDis[i]){
                    minDis[i] = minDis[minInd] + graph[minInd][i];
                    path[i] = minInd;
                }
            }
            // for(int n: minDis) System.out.print(n + " ");
            // System.out.println();
            // for(int n: path) System.out.print(n + " ");
            // System.out.println();
        }
        return minDis;
    }
}