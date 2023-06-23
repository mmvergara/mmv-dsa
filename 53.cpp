
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int maxSubArray(vector<int>& nums) {
	int sum = 0, highest = 0;
	for (int i = 0 ; i < nums.size() ; i++){
		sum = max(nums[i],nums[i]+sum);
		highest = max(highest,sum);
	}
	return highest;
		        
}

int main() {
	vector<int> in1 = {-2,1,-3,4,-1,2,1,-5,4};
	cout << maxSubArray(in1) << "\n";
}
