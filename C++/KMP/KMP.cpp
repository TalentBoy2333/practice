#include<iostream>
#include<string>
using namespace std;
int * get_next(string s);
int kmp(string s1, string s2);

int * get_next(string s){
    int length = s.length();
    int * next = new int[length + 1];
    for(int i = 0; i < length+1; i++){
        next[i] = 0;
    }
    int i = 1, j = 0;
    while(i < length){
        // cout << i << "\t" << j << endl;
        if(j == 0 || s[i-1] == s[j-1]){
            i++;
            j++;
            next[i] = j;
        }else{
            j = next[j];
        }
    }
    return next;
}

int kmp(string s1, string s2){
    int length = s1.length();
    int * next = get_next(s1);
    cout << "next: " << endl;
    for(int i = 0; i < length+1; i++){
        cout << next[i] << "\t";
    }
    cout << endl;

    int i = 0, j = 0;
    while(i < s1.length() && j < s2.length()){
        if(j == 0 || s1[i] == s2[j]){
            i++;
            j++;
        }else{
            j = next[j];
        }
    }
    if(i >= s2.length()){
        return i - s2.length();
    }else{
        return 0;
    }
}


int main(){
    string str1 = "abcababca";
    string str2 = "cab";
    cout << "str1: " << str1 << endl;
    cout << "str2: " << str2 << endl;
    int res = kmp(str1, str2);
    cout << "str2在str1中的位置为: " << res << endl;

    return 0; 
}