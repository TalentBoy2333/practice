public class Kruskal{
    public static void main(String[] args) {
        Edge edges[] = {
            new Edge(4, 7, 7), new Edge(2, 8, 8), new Edge(0, 1, 10),
            new Edge(0, 5, 11), new Edge(1, 8, 12), new Edge(3, 7, 16),
            new Edge(1, 6, 16), new Edge(5, 6, 17), new Edge(1, 2, 18),
            new Edge(6, 7, 19), new Edge(3, 4, 20), new Edge(3, 8, 21),
            new Edge(2, 3, 22), new Edge(3, 6, 24), new Edge(4, 5, 26)
        };

        kruskal(edges);
    }

    static void kruskal(Edge [] edges){
        int parent[] = new int[edges.length];
        for(int i = 0; i < parent.length; i++){
            parent[i] = 0;
        }
        for(int i = 0; i < edges.length; i++){
            int b = edges[i].begin;
            int e = edges[i].end;
            int m = find(parent, b);
            int n = find(parent, e);
            if(m != n){
                parent[m] = n;
                System.out.print("(" + b + ", " + e + ")  ");
            }
        }
        System.out.println();
    }
    static int find(int [] parent, int f){
        while(parent[f] > 0){
            f = parent[f];
        }
        return f;
    }
}

class Edge{
    int begin;
    int end;
    int weight;
    Edge(int b, int e, int w){
        this.begin = b;
        this.end = e; 
        this.weight = w;
    }
}