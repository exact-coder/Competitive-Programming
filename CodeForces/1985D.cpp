#include<bits/stdc++.h>
using namespace std;
#define int long long

int32_t main(){
    int tt; cin >> tt;
    while(tt--){
        int n,m; cin >> n >> m;
        char ch;

        int row1=-1, row2=-1;
        int col1=1e9, col2=-1;
        
        for(int i =0; i<n;i++){
            for(int j=0; j<m; j++){
                cin >> ch;
                if(ch=='#' && row1==-1) row1=i+1;
                if(ch=='#') row2 = i+1;
                if(ch=='#' && col1>j+1) col1 = j+1;
                if(ch=='#' && col2<j+1) col2 = j+1;
            }
        }
        int x = (row1+row2)/2;
        int y = (col1+col2)/2;
        cout << x << ' ' << y << endl;
    }
    return 0;
}
