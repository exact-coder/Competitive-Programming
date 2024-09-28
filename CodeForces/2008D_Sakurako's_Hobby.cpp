/*******************************
Username: JahidHasan90
Problem: https://codeforces.com/problemset/problem/2008/D
Give Time to Time , It can hill everything.
********************************/


#include <bits/stdc++.h>
using namespace std;

int dfs(vector<int> &v,int i,vector<bool> &used,string &s,vector<int> &curr){
    curr.push_back(i);
    if(used[i]) return 0; 
    if(s[i-1] == '0'){
        used[i] = true;
        return 1 + dfs(v,v[i-1],used,s,curr);
    }else{
        used[i] = true;
        return dfs(v,v[i-1],used,s,curr);
    }
    return 0;
    
}

int main()
{
    



    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        vector<int> v(n);
        for(int i = 0; i < n;i++) cin>>v[i];
        string s; cin>>s;
        
        vector<bool> used(n+1,false);
        vector<int> ans(n+1,0);
        for(int i = 1; i <= n; i++){
            
            if(used[i]) continue;
            
            vector<int> curr;
            
            int x = dfs(v,i,used,s,curr);
            for(int a : curr){
                ans[a] = x;
            }
           
            
        }
        for(int i = 1; i <= n;i++){
            cout<<ans[i]<<" ";
        }
        
        
        
        
        
        cout<<"\n";
        
    }

    return 0;
}