#include<bits/stdc++.h>
using namespace std;


/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1977/B
Give Time to Time , It can hill everything.
********************************/


int main(){
    int tc; cin>>tc;
    while (tc--)
    {
        int n; cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        sort(a.begin(), a.end());
        cout << a[0] << " " << a[n - 1] << endl;
    }
    return 0;
}


// g++ Sample.cpp && ./a.exe