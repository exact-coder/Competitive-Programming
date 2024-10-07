#include "bits/stdc++.h";
using namespace std;


int main(){
    int tt; cin >> tt;
    while (tt--)
    {
        ll n,m; cin >> n >> m;
        vector<ll>v(n);
        for(auto &it:v)cin>>it;
        sort(all(v));
        vector<ll>pre(n);
        pre[0]=v[0];
        for(int i=1;i<n;i++){
            pre[i]=pre[i-1]+v[i];
        }
        ll ans=0;
        for (int i = 0; i < n; i++)
        {
            ll temp =(i==0 ? 0:pre[i-1])+m;
            ll idx1= upper_bound(all(v),v[i]+1)-v.begin();
            idx1--;
            ll idx2= upper_bound(all(pre),temp)-pre.begin();
            idx2--;
            
            if(idx2<i)continue;
            if(idx2<=idx1){
                ans=max(ans,pre[idx2]-(i==0 ? 0:pre[i-1]));
            }else
            {
                ans=max(ans,pre[idx1]-(i==0 ? 0:pre[i-1]));
            }
        }

        cout<<ans<<endl;
    }
}
