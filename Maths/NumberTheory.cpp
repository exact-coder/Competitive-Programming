#include "bits/stdc++.h"
using namespace std;

int gcd(int a, int b){
    if(a == 0){
        return b;
    }
    return gcd(b % a, a);
}

int main(){
    /*int n;
    cin >> n;

    int cnt = 0;

    for(int i = 1; i*i <= n; i++){
        if(n % i == 0){
            cnt++;

            if(i != n/i){
                cnt++;
            }
        }

    }
    cout << cnt; */

    // Seen of Eronatishis

    /* vector<int> prime(n+1,1);
    prime[1] 0;

    for(int i = 2; i<=n; i++){
        if(!prime[i]) continue;

        for(int j =i *i; j <=n; j+=i){
            prime[j] = 0;
        }
    } */

    // GCD
    int a,b;
    cin >> a >> b;

    cout << gcd(a,b);

}
