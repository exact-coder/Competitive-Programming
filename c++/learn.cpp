#include <bits/stdc++.h>
using namespace std;

int32_t main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "r", stdout);
    // #endif

    char ch;
    cout<< "Enter Charracter : ";
    cin>>ch;

    if(ch >= 'a' && ch <= 'z'){
        cout<<"LOWERCASE"<<endl;
    }else if(ch >= 65 and ch<=90){
        cout<<"UPPERCASE"<<endl;
    }else{
        cout<<"NOT a character";
    }
}
// g++ learn.cpp && ./a.exe