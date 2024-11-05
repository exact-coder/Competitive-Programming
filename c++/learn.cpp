#include <bits/stdc++.h>
using namespace std;

int decToBinary(int dec){

    int binary=0;
    int power =1;

    while(dec){
        int reminder=dec%2;
        dec /=2;
        binary +=reminder*power;
        power*=10;
    }
    return binary;
}

int binToDecimal(int bin){
    int decimal=0,power=1;
    while (bin)
    {
        int reminder = bin%10;
        decimal +=reminder*power;
        bin /=10;
        power *=2;
    }
    return decimal;
    
}

int32_t main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "r", stdout);
    // #endif
    // cout<<"Type a Number: ";
    // int n;cin>>n;
    // for(int i=0;i<=n;i++){
    //     cout << decToBinary(i) <<endl;
    // }
    cout<<"Give a Binary Number: ";
    int n;cin>>n;
    cout <<binToDecimal(n)<<endl;
    return 0;
}
// g++ learn.cpp && ./a.exe