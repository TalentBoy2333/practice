public class Prim{
    public static void main(String[] args) {
        int [][] graph = {
            {0, 10, 65535, 65535, 65535, 11, 65535, 65535, 65535},
            {10, 0, 18, 65535, 65535, 65535, 16, 65535, 12},
            {65535, 65535, 0, 22, 65535, 65535, 65535, 65535, 8},
            {65535, 65535, 22, 0, 20, 65535, 65535, 16, 21},
            {65535, 65535, 65535, 20, 0, 26, 65535, 7, 65535},
            {11, 65535, 65535, 65535, 26, 0, 17, 65535, 65535},
            {65535, 16, 65535, 65535, 65535, 17, 0, 19, 65535},
            {65535, 65535, 65535, 16, 7, 65535, 19, 0, 65535},
            {65535, 12, 8, 21, 65535, 65535, 65535, 65535, 0}
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

        System.out.println("Prim: ");
        prim(graph);
    }

    static void prim(int [][] graph){
        int adjvex[] = new int[graph.length];
        int lowcost[] = new int[graph.length];
        for(int i = 0; i < graph.length; i++){
            lowcost[i] = graph[0][i];
            adjvex[i] = 0;
        }
        for(int i = 1; i < graph.length; i++){
            int min = 65535;
            int minInd = 0;
            for(int j = 0; j < lowcost.length; j++){
                if(lowcost[j] != 0 && lowcost[j] < min){
                    min = lowcost[j];
                    minInd = j;
                }
            }
            System.out.print("(" + adjvex[minInd] + ", " + minInd + ")  ");
            lowcost[minInd] = 0;
            for(int j = 0; j < lowcost.length; j++){
                if(lowcost[j] != 0 && graph[minInd][j] < lowcost[j]){
                    lowcost[j] = graph[minInd][j];
                    adjvex[j] = minInd;
                }
            }
        }
        System.out.println();
    }
}