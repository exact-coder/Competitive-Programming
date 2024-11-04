#include <bits/stdc++.h>
using namespace std;

int32_t main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "r", stdout);
    // #endif

    int outter;
    cout<<"Lenght of Outter loop: ";
    cin>>outter;

    char ch ='A';
    for (int i = 0; i < outter; i++){
        for(int j =0; j<outter-i-1;j++){
            cout<< " ";
            
        }
        for(int j=0; j<i+1;j++){
            cout<<j;
        }
        for(int j=i; j>0;j--){
            cout<<j;
        }
        cout<<endl;
    }
    
}
// g++ parimid.cpp && ./a.exe