/**********************************DANET**********************************/
#include <bits/stdc++.h>
using namespace std;

#pragma GCC optimize("O3")

/**********************************DEFINES**********************************/
#define Tof_Io  	ios_base::sync_with_stdio(false);cin.tie(0) , cout.tie(0);
#define tolower(x)  transform(x.begin(),x.end(),x.begin(),::tolower);
#define toupper(x)  transform(x.begin(),x.end(),x.begin(),::toupper);
#define kill(x)     cout << x << endl, exit(0)
#define debug(x)    cerr << #x << ": " << x << endl
#define all(x) 		x.begin(),x.end()
#define int 		long long int
#define double  	long double
#define eb			emplace_back
#define pb			push_back
#define mk 			make_pair
#define F 			first
#define S 			second
#define endl 		'/n'
/**********************************UNNESS-DEF**********************************/
#define edge(x,y,adj) adj[x].pb(x) , adj[y].pb(x)
#define tagh2(x) 	x>>1
#define zarb2(x) 	x<<1
/***********************************VARIABLES***********************************/
const int N = 1e6 + 23;
const int maxn = 1e5 + 23;
const int inf = 1e18;
const int mod = 1e9 + 7; //998244353
const int delta = 998244353;
const double PI = 3.141592653589793;
const int LOG = 23;
/***********************************FUNCTION***********************************/
void build(){fac[0] = 1; inv[0] = pwe(fac[0],mod-2);for(int i = 1 ; i< N ; i ++) {fac[i] = (fac[i-1] * i)%mod;inv[i] = pwe(fac[i],mod-2);}}
int lcm(int a, int b) {return a/gcd(a,b)*b;}
int gcd(int a, int b) {return b?gcd(b,a%b):a;}
void print(bool fl){if(fl==0) cout <<"YES";else cout << "NO";}
int C(int n,int r){return fac[n] * inv[r] % mod * inv[n-r] % mod;}
int pwe(int a, int b, int md = mod){int res = 1; while(b){if(b&1){res=(a*res)%md;}a=(a*a)%md;b>>=1;}return(res);}
int lis(vector<int>& v){if (v.size() == 0) {return 0;} vector<int> tail(v.size(), 0); int szgth = 1; tail[0] = v[0]; for (int i = 1; i < v.size(); i++) {auto b = tail.begin(), e = tail.begin() + szgth; auto it = lower_bound(b, e, v[i]); if (it == tail.begin() + szgth){tail[szgth++] = v[i];}else{*it = v[i];}} return szgth;}
/*************************************BUILD*************************************/
int fac[N];
int inv[N];
vector<int> adj[N];
/*************************************SOLVE*************************************/
void solve()
{
	
}
/***********************************MAIN-CODE***********************************/

int32_t main()
{
	Tof_Io;
	int Test_Case = 1;
	cin >> Test_Case;
	while(Test_Case--)
	{
		solve();
		cout << endl;
	}
}

