public class FenWick{
    // 参考: https://blog.csdn.net/bestsort/article/details/80796531
    public static void main(String[] args) {
        int data[] = {1,2,3,4,5,6,7,8}; // 真实存放数据的数组
        int sums[] = getFenWick(data); // 树状数组中求和的数组
        show(data, sums);

        update(1, 1, data, sums);
        show(data, sums);

        for(int i = 0; i < 8; i++){
            System.out.println(getSum(i, sums));
        }
        // 查找一个ind下的值可以通过 getSum(ind, sums) - getSum(ind-1, sums) 得到
    }

    static void show(int [] data, int [] sums){
        System.out.println("data: ");
        for(int n: data) System.out.print(n + "\t");
        System.out.println();
        System.out.println("sums: ");
        for(int n: sums) System.out.print(n + "\t");
        System.out.println();
    }

    static int [] getFenWick(int [] data){
        int sums[] = new int[data.length]; 
        for(int i = 0; i < data.length; i++){
            for(int j = 0; j < lowbit(i+1); j++){
                sums[i] += data[i-j];
            }
        }
        return sums;
    }
    static int lowbit(int x) {
        // 取出x(二进制)的最低位1, 前面的舍去, 得到的十进制数
        // 如: 2 -> 10 return 2(10b);  3 -> 11 return 1(1b);  6 -> 110 return 2(10b);
        return x & (-x);
    }

    static void update(int ind, int update, int [] data, int [] sums){
        // update表示: data[ind] += update;
        data[ind] += update;
        for(int i = ind; i < sums.length; i += lowbit(i+1)){
            sums[i] += update;
        }
    }

    static int getSum(int ind, int [] sums){
        // 计算data[0]到data[ind]之间的和
        int sum = 0;
        for(int i = ind; i > 0; i -= lowbit(i+1)){
            sum += sums[i];
        }
        return sum;
    }
    
}