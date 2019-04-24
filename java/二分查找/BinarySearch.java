public class BinarySearch{
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,6,6,6,6,6,8,9};
        int target = 10;
        for(int n: arr){
            System.out.print(n + " ");
        }
        System.out.println();

        // int index = binarySearch(arr, target);
        // int index = firstEqual(arr, target);
        // int index = firstLargeEqual(arr, target);
        // int index = firstLarge(arr, target);
        // int index = lastEqual(arr, target);
        // int index = lastSmallEqual(arr, target);
        int index = lastSmall(arr, target);

        System.out.println("index: " + index + "\ttarget: " + target);
    }

    static int binarySearch(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] == target)  return mid;
            else if(arr[mid] > target)  high = mid - 1;
            else low = mid + 1;
        }
        return -1;
    }

    static int firstEqual(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] >= target)  high = mid - 1;
            else low = mid + 1;
        }
        if(low < arr.length && arr[low] == target) return low;
        else return -1;
    }

    static int firstLargeEqual(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] >= target)  high = mid - 1;
            else low = mid + 1;
        }
        if(low < arr.length) return low;
        else return -1;
    }

    static int firstLarge(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] > target) high = mid - 1;
            else low = mid + 1;
        }
        if(low < arr.length && arr[low] > target) return low;
        else return -1;
    }
    
    static int lastEqual(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] > target) high = mid - 1;
            else low = mid + 1;
        }
        if(high >= 0 && arr[high] == target) return high;
        else return -1;
    }

    static int lastSmallEqual(int [] arr, int target){
        int low = 0, high = arr.length-1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] > target) high = mid - 1;
            else low = mid + 1;
        }
        if(high >= 0) return high;
        else return -1;
    }

    static int lastSmall(int [] arr, int target){
        int low = 0, high = arr.length - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] >= target) high = mid - 1;
            else low = mid + 1;
        }
        if(high >= 0) return high;
        else return -1;
    }
}