#include<iostream>
using namespace std;

void show_nums(int nums[], int len);
void swap(int nums[], int i, int j);
void bubble_sort(int nums[], int len);

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

void bubble_sort(int nums[], int len){
    for(int i = 0; i < len; i++){
        for(int j = 0; j < i; j++){
            if(nums[i] < nums[j]){
                swap(nums, i, j);
            }
        }
    }
}

int main(){
    int nums[] = {3,5,4,6,8,2,1,9,7};
    int len = sizeof(nums) / sizeof(nums[0]);
    show_nums(nums, len);
    bubble_sort(nums, len);
    show_nums(nums, len);

    return 0;
}