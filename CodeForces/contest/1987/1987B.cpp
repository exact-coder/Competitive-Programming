#include <iostream>
#include<bits/stdc++.h>
using namespace std;
#define int long long



signed main() 
{
    int t;
    cin>>t;
    while(t--){
      
     int n;
     cin>>n;
     vector<int> v(n);
     
     for(auto &val:v) cin>>val;
     
     vector<int> b;
     int x = v[0];
     for(auto &val:v){
       x = max(x,val);
       if(x>val){
         b.push_back(x - val);
       }
     }
     if(b.size()==0){
       cout<<0<<endl;
       continue;
     }
     sort(b.begin(),b.end());
     int ans = b[b.size()-1],y = 0;
     
     for(int i = 0;i<b.size();i++){
       ans+=(b[i] - y)*(b.size()-i);
       y = b[i];
     }
     
    cout<<ans<<endl;
      
    }
    return 0;
}