public class Permutation{
    public static void main(String[] args) {
        // int nums[] = {1,2,3};
        int nums[] = {1,2,2};
        for(int n: nums) System.out.print(n + " ");
        System.out.println();

        System.out.println("All permutation: ");
        // permutation(nums, 0);
        permutation_v2(nums, 0);
    }

    static void swap(int [] nums, int x, int y){
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }

    static void permutation(int [] nums, int index){
    // 标准算法
    // 从n个不同元素中任取m(m<=n)个元素, 按照一定的顺序排列起来, 
    // 叫做从n个不同元素中取出m个元素的一个排列. 当m==n时所有的排列情况叫全排列。
        if(index >= nums.length){
            for(int n: nums){
                System.out.print(n + " ");
            }
            System.out.println();
        }else{
            for(int i = index; i < nums.length; i++){
                swap(nums, index, i);
                permutation(nums, index+1);
                swap(nums, index, i); 
            }
        }
    }

    static void permutation_v2(int [] nums, int index){
    // 去重算法
    // [1,2,2]会产生122, 122, 212, 221, 221, 212含有重复元素的排列
    // 使用该算法(如果i和index之间存在一个数与nums[i]相同, 则不交换)可以避免重复
        if(index == nums.length){
            for(int n: nums) System.out.print(n + " ");
            System.out.println();
        }else{
            for(int i = index; i < nums.length; i++){
                if(isSwap(nums, index, i)){
                    swap(nums, i, index);
                    permutation_v2(nums, index+1);
                    swap(nums, i, index);
                }
            }
        }
    }

    static boolean isSwap(int [] nums, int low, int high){
        for(int i = low; i < high; i++){
            if(nums[i] == nums[high]) return false;
        }
        return true;
    }
}