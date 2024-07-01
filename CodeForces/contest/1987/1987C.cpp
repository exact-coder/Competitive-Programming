#include <bits/stdc++.h>
using namespace std;
#define IOS ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define ll long long


int main(){
    IOS
    ll t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        ll maxx=0;
        ll ans=0;
        ll more=0;
        for(ll i=0;i<n;++i){
            ll x;
            cin>>x;
            ans = max(ans, x + i); 
        }
        cout<<ans<<endl;
    }
}