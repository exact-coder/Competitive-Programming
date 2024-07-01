#include <bits/stdc++.h>
using namespace std;
#define N 5010
using ll = long long;
ll dp[N][N];
ll ct[N];
#define DP dp[i][asc]
ll r(ll i, ll asc)
{
    if (asc < 0)
        return -2;
    if (!i)
        return asc ? -2 : 0;
    if (~DP)
        return DP;
    if (ct[i])
        DP = r(i - 1, asc - 1);
    else
        DP = r(i - 1, asc);
    if (r(i - 1, asc) != -2 && r(i - 1, asc) + ct[i] <= asc)
    {
        if (DP == -2 || r(i - 1, asc) + ct[i] < DP)
        {
            DP = r(i - 1, asc) + ct[i];
        }
    }
    return DP;
}
int main()
{
    int tc;
    cin >> tc;
    while (tc--)
    {
        ll n;
        cin >> n;
        for(int i = 0; i <= n; i++) 
            fill_n(dp[i], n + 1, -1);
        for(int i = 0; i < n ;i++) { 
            ll x;
            cin >> x;
            ct[x]++; 
        }
        ll ans = n;
        for(int i = n; i >= 0; i--)
            if (r(n, i) != -2) ans = i;
        cout << ans << '\n';
        fill_n(ct, n + 1, 0ll);
    }
}