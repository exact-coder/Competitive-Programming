#include <bits/stdc++.h>
using namespace std;

int factorial(int n){
    int fact = 1;
    for(int i=1;i<=n;i++){
        fact *=i;
    }
    return fact;
}

int sumOfDigits(int num){
    int digSum=0;
    while(num>0){
        int lastDig = num%10;
        num /= 10;
        digSum +=lastDig;
    }

    return digSum;
}

int nCr(int n,int r){
    int fact_n = factorial(n);
    int fact_r = factorial(r);
    int fact_nMINUSr = factorial(n-r);
    return fact_n / (fact_r * fact_nMINUSr);
    
}

int32_t main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "r", stdout);
    // #endif
    cout << "Put a numbers : ";
    int num; cin >>num;
    // cout <<"The factorial is : "<< factorial(num) << endl;
    cout <<"All Digits sum is : "<< sumOfDigits(num) << endl;
    cout <<"nCr is : "<< nCr(10,8) << endl;

    
    return 0;
}
// g++ learn.cpp && ./a.exe