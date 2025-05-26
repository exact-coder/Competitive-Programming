#include<bits/stdc++.h>
using namespace std;

int main(){
    int testcase; cin >> testcase;
    
    while(testcase--){
        int n; cin >> n;
        string str; cin >> str;

        for(int i =0; i<n;i++){
            if(str[i] == 'b'|| str[i] == 'c' || str[i] == 'd'){
                cout << str[i];
            }else{
                cout << str[i];
                if(str[i+1] == 'b' || str[i+1] == 'c' || str[i+1] == 'd'){
                    if(str[i+2] != 'a' && str[i+2] != 'e'){
                        cout << str[i+1];
                        i+=1;
                    }
                }
                if(i!=n-1) cout << '.';
            }
        }
        cout << endl;
    }
}