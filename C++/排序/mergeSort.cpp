#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void merge_sort(int nums[], int l, int r);
void merge(int nums[], int l, int mid, int r);

void show_nums(int nums[], int len){
    for(int i = 0; i < len; i++){
        cout << nums[i] << "\t";
    }
    cout << endl;
}

void merge(int nums[], int l, int mid, int r){
    int temp[r-l+1];
    int ind = 0;
    int i1 = l, i2 = mid+1;
    while(i1 <= mid && i2 <= r){
        if(nums[i1] < nums[i2]){
            temp[ind] = nums[i1];
            i1++;
        }else{
            temp[ind] = nums[i2];
            i2++;
        }
        ind++;
    }
    while(i1 <= mid){
        temp[ind] = nums[i1];
        i1++;
        ind++;
    }
    while(i2 <= r){
        temp[ind] = nums[i2];
        i2++;
        ind++;
    }
    for(int i = 0; i < r-l+1; i++){
        nums[i+l] = temp[i];
    }
}

void merge_sort(int nums[], int l, int r){
    if(l < r){
        int mid = (l + r) / 2;
        merge_sort(nums, l, mid);
        merge_sort(nums, mid+1, r);
        merge(nums, l, mid, r);
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    merge_sort(nums, 0, len-1);
    show_nums(nums, len);

    return 0;
}