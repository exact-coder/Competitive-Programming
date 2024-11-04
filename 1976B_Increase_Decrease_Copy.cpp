#include<bits/stdc++.h>
using namespace std;



/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1976/B
Give Time to Time , It can hill everything.
********************************/



int main(){
    int tc; cin>>tc;
    while (tc--)
    {
        int n; cin>>n;
        vector<int>a(n),b(n+1);

        for (int i=0; i<a.size(); i++) {
            cin >> a[i];
        }

        for (int i=0; i<b.size(); i++) {
            cin >> b[i];
        }

        int tot=1;
        for (int i=0;i<n;i++){
            tot+=abs(a[i]-b[i]);
        }
        int mn = INT_MAX;
        for(int i=0;i<n;i++){
            if(a[i]<=b[n] && b[n]<=b[i]) mn=0;
            if(a[i]>=b[n] && b[n]>=b[i]) mn=0;
        }
        for(int i=0;i<n;i++){
            if(a[i]<=b[n] && a[i]<=b[i]) mn=min(mn,abs(b[n]-b[i]));
            if(a[i]>=b[n] && a[i]>=b[i]) mn=min(mn,abs(b[n]-b[i]));
        }
        for(int i=0;i<n;i++){
            mn=min(mn,abs(b[n]-a[i]));
        }
        cout << tot+mn <<"\n";
    }
    return 0;
}



// g++ learn.cpp && ./a.exe