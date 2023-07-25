#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


vector<int> twoSum(vector<int> arr, int t){
	unordered_map <int,int> cs;

	for (int i = 0; i < arr.size(); i++){
		int com = t - arr[i];

		if (cs.find(com) != cs.end()){
			vector<int> ans = { i, cs[com] };	
			return ans;
		} else {
			cs[arr[i]] = i;
		};

	};
	vector<int> ans = {-1,-1};
	return ans;
}


int main(){
	vector<int> arr = {1,2,3,4,5};
	int t = 91;

	vector<int> res = twoSum(arr,t);

	for (int i = 0; i < res.size(); i++){
		cout << res[i] << "\n";
	}

	return 0;
} 
