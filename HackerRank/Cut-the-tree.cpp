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


long recdfs(int current,long sum,int w[]){
    number+=1;
    visited.insert(current);
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
        if (g.find(a)==g.end()){
            g.insert(make_pair(a,vector<int>()));
            
            g[a].push_back(b);
            
        }
        else g[a].push_back(b);
        if (g.find(b)==g.end()){
            g.insert(make_pair(b,vector<int>()));
            g[b].push_back(a);
        }
        else g[b].push_back(a);
    }
    r=recdfs(2,sum,w);
    long m=sum;
    for (int i=1;i<N+1;i++){
        m=min(m,abs(sum-2*sols[i]));
        
    }
    cout<<m;
    return 0;
}
