import java.util.LinkedList;
import java.util.Queue;

public class TopologySort{
    public static void main(String[] args) {
        int graph[][] = { // 图邻接矩阵, 1表示第i行到第j列有连接
            {0, 1, 1, 1, 0, 0},
            {0, 0, 0, 0, 0, 0},
            {0, 1, 0, 0, 1, 0},
            {0, 0, 0, 0, 1, 0},
            {0, 0, 0, 0, 0, 0},
            {0, 0, 0, 1, 1, 0}
        };
        System.out.println("Graph: ");
        char ch[] = {'a', 'b', 'c', 'd', 'e', 'f'};
        System.out.print("\t");
        for(int i = 0; i < ch.length; i++){
            System.out.print(ch[i] + "\t");
        }
        System.out.println();
        for(int i = 0; i < graph.length; i++){
            System.out.print(ch[i] + "\t");
            for(int j = 0; j < graph[0].length; j++){
                System.out.print(graph[i][j] + "\t");
            }
            System.out.println();
        }

        System.out.println("In: "); // 入度
        int in[] = calIn(graph);
        for(int i = 0; i < ch.length; i++){
            System.out.print(ch[i] + "\t");
        }
        System.out.println();
        for(int n: in) System.out.print(n + "\t");
        System.out.println();

        System.out.println("Topology Sort: ");
        topologySort(graph, in, ch);
    }

    static int [] calIn(int [][] graph){
        int in[] = new int[graph.length];
        for(int i = 0; i < graph[0].length; i++){
            for(int j = 0; j < graph.length; j++){
                in[i] += graph[j][i];
            }
        }
        return in;
    }

    static void topologySort(int [][] graph, int [] in, char [] ch){
        // 参考: https://blog.csdn.net/qq_41713256/article/details/80805338
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < ch.length; i++){
            if(in[i] == 0) q.add(i);
        }
        while(!q.isEmpty()){
            int cur = q.poll();
            System.out.print(ch[cur] + "\t");
            for(int i = 0; i < graph[0].length; i++){
                if(graph[cur][i] == 1){
                    in[i]--;
                    if(in[i] == 0) q.add(i);
                } 
            }
        }
        System.out.println();
    }
}