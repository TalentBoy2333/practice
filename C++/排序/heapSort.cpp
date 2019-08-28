#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void heap_adjust(int nums[], int start, int end);
void heap_sort(int nums[], int len);

void show_nums(int nums[], int len){
    for(int i = 0; i < len; i++){
        cout << nums[i] << "\t";
    }
    cout << endl;
}

void swap(int nums[], int i, int j){
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}

/**
 * 表示调整大顶堆的函数
 * 对数组start位置的节点进行调整, 使其成为大顶堆
 * 注意: start是从1开始计数的, 这样方便理解大顶堆, 
 * 因此, 在对数组进行操作的时候需要注意下标-1. 
 */
void heap_adjust(int nums[], int start, int end){
    int temp = nums[start-1];
    int ind = start;
    while(ind <= end/2){
        if(2*ind+1 > end){
            if(nums[ind - 1] > nums[2*ind - 1]){
                break;
            }else{
                swap(nums, 2*ind - 1, ind - 1);
                ind = 2 * ind;
            }
        }else{
            if(nums[ind - 1] > nums[2*ind - 1] && nums[ind-1] > nums[2*ind+1 - 1]){
                break;
            }
            if(nums[2*ind - 1] > nums[2*ind+1 - 1]){
                swap(nums, 2*ind - 1, ind - 1);
                ind = 2 * ind;
            }else{
                swap(nums, 2*ind+1 - 1, ind - 1);
                ind = 2 * ind + 1;
            }
        }
    }
}

void heap_sort(int nums[], int len){
    for(int i = len / 2; i >= 1; i--){
        heap_adjust(nums, i, len);
    }
    // show_nums(nums, len);
    for(int i = len; i > 1; i--){
        swap(nums, 0, i - 1);
        heap_adjust(nums, 1, i-1);
        // show_nums(nums, len);
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    heap_sort(nums, len);
    show_nums(nums, len);

    return 0;
}