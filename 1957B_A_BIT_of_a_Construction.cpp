#include<bits/stdc++.h>
using namespace std;


/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1957/B
Give Time to Time , It can hill everything.
********************************/


int main(){
    int tc; cin>>tc;
    while (tc--){
        long long n,k;
        cin >> n >>k;
        long long mx = -1, st=0;
        for (long long i = 0; i <= 30; i++)
        {
            if((k & (1<<i))){
                mx = i;
                st++;
            }
        }

        if(n==1 || mx+1 == st){
            cout<<k<<" ";
            for (long long i = 1; i < n; i++) cout<<0<<" ";
            cout<<endl;
        }else{
            long long val = (1<<mx)-1;
            long long extra = k-val;

            cout<<val<<" "<<extra<<" ";
            for(long long i =1;i<n-1;i++){ cout<<0<<" ";}
            cout<<endl;
        }

    }
    return 0;
}


// g++ learn.cpp && ./a.exe





