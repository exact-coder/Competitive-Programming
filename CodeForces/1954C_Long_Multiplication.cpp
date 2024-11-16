#include<bits/stdc++.h>
using namespace std;


/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1954/C
Give Time to Time , It can hill everything.
********************************/


int main(){
    int tc; cin>>tc;
    while (tc--)
    {
        string x,y;
        cin>>x>>y;
        long long n = x.size();

        long long f =0;

        for(long long i = 0;i<n;i++){
            long long c= x[i]-48;
            long long d= y[i]-48;

            if(c==d) continue;
            if(f==0){
                if(c<d) swap(x[i],y[i]);
                f=1;
            }else {
                if(c>d) swap(x[i],y[i]);
            }
        }

        cout<<x<<endl;
        cout<<y<<endl;
    }

    return 0;
}


// g++ learn.cpp && ./a.exe