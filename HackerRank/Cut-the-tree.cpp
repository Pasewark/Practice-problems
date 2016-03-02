#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <set>
using namespace std;
map<int,int> sols;
set<int> visited;
map<int,vector<int>> g;
int number;
/*long sol(map<int,vector<int>> g,int n,long sum,int w[]){
    map<int,int> sols;
    for (int i=0;i<n;i++){
        
    }
}*/

long recdfs(int current,long sum,int w[]){
    number+=1;
    visited.insert(current);
    //cout<<number<<" "<<current<<endl;
    if (sols.find(current)!=sols.end()){
        return sols[current];
    }
    if (g[current].size()==1&&visited.find(g[current][0])!=visited.end()){
        sols[current]=w[current-1];
        return sols[current];
    }
    long csum=0;
    for (int i=0;i<g[current].size();i++){
        if (visited.find(g[current][i])==visited.end()) csum+=recdfs(g[current][i],sum,w);
    }
    csum+=w[current-1];
    sols[current]=csum;
    return sols[current];
}

/*long dfs(int b,long sum,int w[]){
    int a,add;
    map<int,int> sols;
    stack<int> s;
    set<int> visited;
    int current;
    s.push(b);
    while (!s.empty()){
        add=0;
        current=s.top();
        s.pop();
        if (visited.find(current)!=visited.end()) {
            continue;
        }
        visited.insert(current);
        for (int i=0;i<gr[current].size();i++){
            if (visited.find(gr[current][i])==visited.end()){
                add=1;
                s.push(gr[current][i]);
            } 
        }
        if (add==0&&gr[current].size()==1){
            
        }
    }
    for (set<int>::iterator it=visited.begin(); it!=visited.end(); ++it)
        cout << ' ' << *it;
    int si=visited.size();
    cout<<"size"<<si<<endl;
    return 0;
}*/

int main() {
    int N,a,b;
    long sum,r;
    cin>>N;
    int w[N];
    sum=0;
    number=0;
    for (int i=0;i<N;i++){
        cin>>w[i];
        sum+=w[i];
    }
    for (int i=0;i<N-1;i++){
        cin>>a>>b;
        //cout<<a<<b<<endl;
        //if (g.find(2)==g.end()) cout<<"hi";
        if (g.find(a)==g.end()){
            g.insert(make_pair(a,vector<int>()));
            
            g[a].push_back(b);
            
            //c=g[a][0];
            //cout<<c<<endl;
        }
        else g[a].push_back(b);
        if (g.find(b)==g.end()){
            g.insert(make_pair(b,vector<int>()));
            g[b].push_back(a);
        }
        else g[b].push_back(a);
    }
    //cout<<2<<endl;
    //g.empty();
    //ut<<c;
    r=recdfs(2,sum,w);
    long m=sum;
    for (int i=1;i<N+1;i++){
        //cout<<i<<" "<<sols[i]<<endl;
        m=min(m,abs(sum-2*sols[i]));
        
    }
    //dfs(g,1);
    cout<<m;
    return 0;
}
