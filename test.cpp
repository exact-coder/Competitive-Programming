#include "bits/stdc++.h"
using namespace std;


int main(){
    int tt; cin >> tt;
    while (tt--)
    {
        int n; cin >> n;
        vector<int>vec(n);
        for(int i = 1; i<n;i++) cin >> vec[i];

        vector<int>answer(n);
        answer[n-1] = 1e9;
        for(int i=n-2;i>=0;i--)
            answer[i] = answer[i+1]-vec[i+1];
        
        for(auto it:answer) cout << it << ' ';
        cout << endl;
    }
}
