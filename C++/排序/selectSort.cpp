#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void select_sort(int nums[], int len);

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

void select_sort(int nums[], int len){
    for(int i = 0; i < len-1; i++){
        int min_ind = i;
        for(int j = i+1; j < len; j++){
            if(nums[j] < nums[min_ind]){
                min_ind = j;
            }
        }
        swap(nums, min_ind, i);
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    select_sort(nums, len);
    show_nums(nums, len);

    return 0;
}