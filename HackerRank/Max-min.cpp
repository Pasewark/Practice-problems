#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
#include <array>
using namespace std;

int main() {
    int N, K, unfairness = INT_MAX;
    long long current1,current2,a,b;
    a=b=0;
    long long temp;
    cin >> N >> K;
    vector<long long> list;
    for (int i=0; i<N; i++){
        cin >> temp;
        
        list.push_back(temp);
    }
    sort(list.begin(),list.end());
    //for (int i=0;i<list.size();i++){
    //    cout<<list[i]<<endl;
    // }
    current2=K-1;
    current1=0;
    int best2=current2;
    long long best=list[current2]-list[current1];
    while (current2<list.size()){
        if (best>list[current2]-list[current1]){
            best=list[current2]-list[current1];
            best2=current2;
        }
        current2++;
        current1++;
    }
    //cout<<current1<<" "<<current2<<endl;
    //cout<<list[current1]<<" "<<list[current2]<<endl;
    cout << best << "\n";
    return 0;
}
