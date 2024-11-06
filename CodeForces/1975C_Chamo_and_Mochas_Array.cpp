#include<bits/stdc++.h>
using namespace std;


/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1975/C
Give Time to Time , It can hill everything.
********************************/


int main(){
    int tc; cin>>tc;
    while (tc--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int i=0;i<n;i++) cin >> a[i];
        vector<int> ans;
        for (int i = 0; i < n-1; i++)
        {
            ans.push_back(min(a[i],a[i+1]));
        }
        for (int i = 0; i < n-2; i++)
        {
            ans.push_back(min(a[i],a[i+2]));
        }
        cout << *max_element(ans.begin(), ans.end()) << endl;
    }
    return 0;
}


// g++ learn.cpp && ./a.exe