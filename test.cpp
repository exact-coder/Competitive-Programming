#include "bits/stdc++.h";
#include <iostream>;
#include <algorithm>; 
using namespace std;

constexpr auto lcm(auto x, auto... xs)
{
    return ((x = std::lcm(x, xs)), ...);
}


int main(){
    int tt; cin >> tt;
    while (tt--)
    {
        int n;
        cin >> n;
        vector <int> v(n);

        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        int x = v[0];
        for(int i =1; i<n;i++){
            x = lcm(x,v[i]);
        }
        vector <int> a(n);
        int sum =0;
        for(int i=0; i<n;i++){
            a[i] = x/v[i];
        }
        if(accumulate(a.begin(),a.end(),0ll) >= x){
            cout<<"-1\n";
            continue;
        }
        for(auto x:a){
            cout <<x<<" ";
        }
        cout << "\n";
        
    }
}
