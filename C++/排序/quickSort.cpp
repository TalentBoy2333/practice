#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void insert_sort(int nums[], int len);
int partation(int nums[], int l, int r);

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

int partation(int nums[], int l, int r){
    int low = l;
    int high = r;
    while(low < high){
        while(low < high && nums[high] >= nums[low]){
            high--;
        }
        swap(nums, low, high);
        while(low < high && nums[low] <= nums[high]){
            low++;
        }
        swap(nums, low, high);
    }
    return low;
}

void quick_sort(int nums[], int l, int r){
    if(l < r){
        int mid = partation(nums, l, r);
        quick_sort(nums, l, mid-1);
        quick_sort(nums, mid+1, r);
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    quick_sort(nums, 0, len-1);
    show_nums(nums, len);

    return 0;
}