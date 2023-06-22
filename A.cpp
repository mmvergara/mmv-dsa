
#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>
#include <unordered_map>

using namespace std;


vector<int> twoSum(vector<int> nums, int target){
	unordered_map<int,int> cs = {};

	for (int i = 0; i < nums.size(); i++){
		int complement = target - nums[i];
		if (cs.find(complement) != cs.end()){
			return {i,cs[complement]};
		}
		cs[nums[i]] = i;
	}
	return {-1,-1};
}

int main(){
	vector<int> inp = {1,2,3,4};
	vector<int> res = twoSum(inp,7);
	cout << res[0] << res[1] << endl;
	return 0;

}
