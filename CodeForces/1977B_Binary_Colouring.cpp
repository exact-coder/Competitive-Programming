#include<bits/stdc++.h>
using namespace std;

/* ******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/1977/B
Give Time to Time , It can hill everything.
********************************/

int main(){
    int tc; cin>>tc;
    while (tc--)
    {
        int x; cin>>x;
        vector<int> vc;

        while(x){
            if(x%2==0) vc.push_back(0);
            else vc.push_back(1);
            x=x/2;
        }
        vc.push_back(0);
        for(int i=0;i<vc.size()-1;++i){
            if (vc[i] == 1 && vc[i+1] ==1){
                for(int j=i; j<vc.size(); ++j){
                    if(vc[j] ==0){
                        vc[j] =1;
                        vc[i]=-1;
                        break;
                    }
                    else{
                        vc[j]=0;
                    }
                }
            }
        }
        cout<<vc.size()<<endl;
        for(int i=0; i<vc.size();++i){
            cout<<vc[i]<<" ";
        }cout<<endl;
    }
    return 0;
    
}





