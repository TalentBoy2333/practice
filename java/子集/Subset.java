public class Subset{
    public static void main(String[] args) {
        int nums[] = {1,2,3};
        for(int n: nums) System.out.print(n + " ");
        System.out.println();

        System.out.println("All subset:");
        subset(nums);
    }

    static void subset(int [] nums){
        int subsetLen = (int)Math.pow(2, nums.length);
        for(int i = 0; i < subsetLen; i++){
            int temp = i;
            for(int j = 0; j < nums.length; j++){
                if(temp % 2 == 1){
                    System.out.print(nums[j]);
                }
                temp /= 2;
            }
            System.out.println();
        }
    }
}