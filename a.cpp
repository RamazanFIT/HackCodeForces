#include<bits/stdc++.h>
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
 
using namespace std;
 
using ll = long long;
using db = long double;
using vi = vector<int>;
using vl = vector<ll>;
using vd = vector<db>;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using pdd = pair<db,db>;
const int INF=0x3fffffff;
// const int MOD=1000000007;
const int MOD=998244353;
const ll LINF=0x1fffffffffffffff;
const db DINF=numeric_limits<db>::infinity();
const db EPS=1e-9;
const db PI=acos(db(-1));
 
void runcase(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    auto calc=[&](const string &t){
        int cnt=0;
        for(int i=0;i<n;i++)if(s[i]!=t[i]&&++cnt>1)return false;
        return true;
    };
    for(int i=1;i<n;i++)if(n%i==0){
        string t="",k=s.substr(0,i);
        for(int j=0;j<n;j+=i)t+=k;
        if(calc(t))return void(cout << i << "\n");
        t="",k=s.substr(n-i,i);
        for(int j=0;j<n;j+=i)t+=k;
        if(calc(t))return void(cout << i << "\n");
    }
    cout << n << "\n";
}
 
int main(){
    cin.tie(nullptr)->sync_with_stdio(false);
    int t(1);
    cin >> t;
    while(t--)runcase();
}