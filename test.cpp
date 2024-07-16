#include "bits/stdc++.h"
using namespace std;


int main(){
    int tt; cin >> tt;
    while (tt--)
    {
        int x,y,i;
        cin >> x >> y;
        int max1 = max(x,y);
        int min1 = min(x,y);
        vector<int> v ,v1;

        while (x)
        {
            int ok = x%2;
            v.push_back(ok);
            x=x/2;
        }
        while (v.size()<32)
        {
            v.push_back(0);
        }
        while (y)
        {
            int ok = y%2;
            v1.push_back(ok);
            y=y/2;
        }
        while (v1.size()<32)
        {
            v1.push_back(0);
        }
        int ans=0;

        for (i = 0; i < 32; i++)
        {
            if(v[i]==v1[i]){
                ans++;
            }else{
                break;
            }
        }
        int ok = (1LL<<ans);
        cout<<ok<<endl;
        
    }
    return 0;
    
}
