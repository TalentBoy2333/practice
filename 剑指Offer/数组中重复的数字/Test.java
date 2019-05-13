public class Test{
    public static void main(String[] args) {
        int a[] = new int[0];
        int duplication[] = new int[1];
        Solution s = new Solution();
        boolean res = s.duplicate(a, 0, duplication);
        System.out.println(res);
        System.out.println(duplication[0]);
    }
}