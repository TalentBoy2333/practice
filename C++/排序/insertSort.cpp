#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void insert_sort(int nums[], int len);

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

void insert_sort(int nums[], int len){
    for(int i = 1; i < len; i++){
        int cur = nums[i];
        int j = i - 1;
        for(; j >= 0; j--){
            if(nums[j] > cur){
                nums[j+1] = nums[j];
            }else{
                break;
            }
        }
        nums[j+1] = cur;
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    insert_sort(nums, len);
    show_nums(nums, len);

    return 0;
}