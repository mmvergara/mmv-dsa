#include <iostream>
#include <vector>
using namespace std;

// Two sum but with a sorted array, initialize right and left pointer
// increment left pointer to increase the sum if sum < target
// decrement right pointer to decrease the sum if sum > target

vector<int> twoSum(vector<int>& nums, int target) {
	int left = 0;
	int right = nums.size()-1;
	
	while (left < right){
		int sum = nums[left] + nums[right];
		if (sum == target){
			return {left,right};
		}

		if (sum > target){
			right--;
		} else {
			left++;
		}
	}
	return {-1,-1};
}

int main() {
	vector<int> arr = {2,7,11,15};
	int target = 9;

	cout << arr[1] << endl;

	vector<int> res = twoSum(arr,target);
	cout << res[0] << " " << res[1] << "\n";
	return 0;
}


