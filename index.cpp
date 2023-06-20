
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> ts(vector<int>& ns, int t) {
	int l = 0;
	int r = ns.size()-1;
	
		while (l < r){
		int s = ns[l] + ns[r];
		if (s == t){
			return {l,r};
		}

		if (s > target){
			r--;
		} else {
			l++;
		}
	}
	return {-1,-1,};
}

int main() {
	cout << "y";
	vector<int> arr = {2,7,11,15};
	int target = 9;
	vector<int> res = twoSum(arr,target);
	cout << res[0] << " " << res[1];

	return 0;
}

