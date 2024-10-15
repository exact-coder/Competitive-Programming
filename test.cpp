#include "bits/stdc++.h";
using namespace std;


int main(){
    int tt; cin >> tt;
    while (tt--)
    {
        long long n,l,r;
        cin >> n >> l >> r;
        vector<long long>v(n);
        for (long long i=0; i<n; i++){
            cin >> v[i];
        }

        long long i=0, j=0;
        long long sum=0;
        long long ans =0;
        while (j != (n +1))
        {
            if (sum >= l && sum <= r){
                ans++;
                sum =0;
                i=j;
            }
            else if (sum < l){
                sum = sum + v[j];
                j++;
            }else{
                sum = sum - v[i];
                i++;
            }
        }


        cout<<ans<<endl;
    }
}
