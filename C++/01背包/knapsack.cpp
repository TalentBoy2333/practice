#include<iostream>
using namespace std;

int dp(int w[], int v[], int n, int c){
    int m[n][c+1];
    for(int i = 0; i < c+1; i++){
        if(i >= w[0]){
            m[0][i] = v[0];
        }
    }
    for(int i = 1; i < n; i++){
        for(int j = 1; j < c+1; j++){
            if(w[i] <= j){
                int val_0 = m[i-1][j]; // 表示不拿第i个物品的最大价值
                int val_1 = m[i-1][j-w[i]] + v[i]; // 表示拿了第i个物品的最大价值
                m[i][j] = max(val_0, val_1);
            }else{
                m[i][j] = m[i-1][j];
            }
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < c+1; j++){
            cout << m[i][j] << "\t";
        }
        cout << endl;
    }
    return m[n-1][c];
}

int main(){
    // 背包问题: 给定一组物品，每种物品都有自己的重量和价格，在限定的总重量内，
    //          我们如何选择，才能使得物品的总价格最高。
    // w: 物品重量
    // v: 物品价值
    // n: 物品种类(编号0 ~ n-1)
    // c: 背包容量(0 ~ c)
    // m: 在装入第i种物品时，容量为j的背包能拥有的最大价值
    int w[] = {4,6,2,2,5,1}; 
    int v[] = {8,10,6,3,7,2};
    int n = 6, c = 12;
    int res = dp(w, v, n, c);
    cout << "能够获取的最大价值为" << res << endl;
    
    return 0;
}