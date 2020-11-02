#include <bits/stdc++.h>
#include <random>
#include <io.h>
using namespace std;

typedef long long ll;

const int maxN=1e5;
const ll maxA=1e9;
const string task_name="SUPSUB";

mt19937 generator(time(0));
ll rand_range(ll mn, ll mx){
	uniform_int_distribution<long long>  distr(mn, mx);
	return distr(generator);
}

void gen_test(int index, int n, int _maxA){
	string index_str = to_string(index);
	while(index_str.length()<2) index_str = "0"+index_str;
	string folder_name = task_name + index_str;
	string output_file = "./"+folder_name+"/"+task_name+".INP";
	mkdir(folder_name.c_str());
	ofstream fo(output_file);
	fo<<n<<'\n';
	for (int i=0; i<n; ++i){
		fo<<rand_range(-_maxA, _maxA)<<' ';
	}
	fo.close();
}

int n;
ll S[maxN+5], T[maxN+5];
ll ans;

void solve(int index){
	string index_str = to_string(index);
	while(index_str.length()<2) index_str = "0"+index_str;
	string folder_name = task_name + index_str;
	string input_file = "./"+folder_name+"/"+task_name+".INP";
	string output_file = "./"+folder_name+"/"+task_name+".OUT";
	ifstream fi(input_file);
	ofstream fo(output_file);
	fi>>n;
	for (int i=1; i<=n; ++i){
		fi>>S[i];
		S[i]+=S[i-1];
		T[i]=T[i-1] + S[i];
	}
	ans=-1e18;
	for (int i=1; i<=n; ++i){
		for (int j=i; j<=n; ++j){
			ans = max(ans, T[j]-(j-i+1)*S[i-1]-T[i-1]);
		}
	}
	fo<<ans;
	fi.close();
	fo.close();
}

int main(){
	for (int i=0; i<100; ++i){
		cout<<"Generating test "<<i<<'\n';
		gen_test(i, 1000*(i+1), maxA);
		cout<<"Solving test "<<i<<'\n';
		solve(i);
	}
}