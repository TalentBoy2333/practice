public class Sort{
    public static void main(String[] args) {
        int arr[] = {3,5,4,6,8,2,1,9,7};
        for(int n:arr){
            System.out.print(n + " ");
        }
        System.out.println();

        // bubbleSort(arr);
        // selectSort(arr);
        // insertSort(arr);
        // shellSort(arr);
        // quickSort(arr, 0, arr.length-1);
        // mergeSort(arr, 0, arr.length-1);
        heapSort(arr);

        for(int n:arr){
            System.out.print(n + " ");
        }
        System.out.println();
    }
    // 交换
    static void swap(int [] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    // 冒泡排序
    static void bubbleSort(int [] arr){
        for(int end = arr.length-1; end > 0; end--){
            boolean flag = true;
            for(int i = 0; i < end; i++){
                if(arr[i] > arr[i+1]){
                    swap(arr, i, i+1);
                    flag = false;
                }
            }
            if(flag){
                break;
            }
        }
    }
    // 选择排序
    static void selectSort(int [] arr){
        for(int i = 0; i < arr.length; i++){
            int min = arr[i], minIndex = i;
            for(int j = i+1; j < arr.length; j++){
                if(arr[j] < min){
                    min = arr[j];
                    minIndex = j;
                }
            }
            swap(arr, i, minIndex);
        }
    }
    // 插入排序
    static void insertSort(int [] arr){
        for(int i = 1; i < arr.length; i++){
            int num = arr[i], j;
            for(j = i-1; j >= 0 && arr[j] > num; j--){
                arr[j+1] = arr[j];
            }
            arr[j+1] = num;
        }
    }
    // 希尔排序
    static void shellSort(int [] arr){
        for(int g = arr.length; g > 0; g /= 2){
            for(int end = g; end < arr.length; end++){
                int num = arr[end], j;
                for(j = end-g; j >= 0 && arr[j] > num; j -= g){
                    arr[j+g] = arr[j];
                }
                arr[j+g] = num;
            }
        }
    }
    // 
    static void quickSort(int [] arr, int s, int e){
        if(s < e){
            int mid = quickSortPart(arr, s, e);
            quickSort(arr, s, mid-1);
            quickSort(arr, mid+1, e);
        }
    }
    static int quickSortPart(int [] arr, int s, int e){
        int low = s, high = e, num = arr[s];
        while(low < high){
            while(arr[high] >= num && low < high){
                high--;
            }
            swap(arr, low, high);
            while(arr[low] <= num && low < high){
                low++;
            }
            swap(arr, low, high);
        }
        return low;
    }
    // 归并排序
    static void mergeSort(int [] arr, int s, int e){
        if(s >= e){
            return;
        }else{
            int mid = (s + e) / 2;
            mergeSort(arr, s, mid);
            mergeSort(arr, mid+1, e);
            merge(arr, s, mid, e);
        }
    }
    static void merge(int [] arr, int s, int m, int e){
        int temp[] = new int[e-s+1];
        int ind1 = s, ind2 = m+1;
        int index = 0;
        while(ind1 <= m && ind2 <= e){
            if(arr[ind1] < arr[ind2]){
                temp[index++] = arr[ind1++];
            }else{
                temp[index++] = arr[ind2++];
            }
        }
        while(ind1 <= m) temp[index++] = arr[ind1++];
        while(ind2 <= e) temp[index++] = arr[ind2++];
        for(int i = s; i <= e; i++) arr[i] = temp[i-s];
    }
    // 
    // static void heapSort(int [] arr){
    //     for(int i = arr.length/2; i > 0; i--){
    //         heapAdjust(arr, i, arr.length-1);
    //     }
    //     for(int i = arr.length-1; i > 1; i--){
    //         swap(arr, 1, i);
    //         heapAdjust(arr, 1, i-1);
    //     }
    // }
    // static void heapAdjust(int [] arr, int s, int e){
    //     int temp = arr[s], j;
    //     for(j = 2*s; j <= e; j *= 2){
    //         if(j+1 <= e && arr[j+1] > arr[j]){
    //             j++;
    //         }
    //         if(temp > arr[j]){
    //             break;
    //         }
    //         arr[s] = arr[j];
    //         s = j;
    //     }
    //     arr[s] = temp;
    // }
    static void heapSort(int [] arr){
        for(int i = arr.length/2; i > 0; i--){
            heapAdjust(arr, i, arr.length-1);
        }
        for(int i = arr.length-1; i > 0; i--){
            swap(arr, 0, i);
            heapAdjust(arr, 1, i-1);
        }
    }
    static void heapAdjust(int [] arr, int s, int e){
        int temp = arr[s-1], j;
        for(j = 2*s; j <= e; j *= 2){
            if(j <= e && arr[j] > arr[j-1]){
                j++;
            }
            if(temp > arr[j-1]){
                break;
            }
            arr[s-1] = arr[j-1];
            s = j;
        }
        arr[s-1] = temp;
    }


}