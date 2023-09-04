#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Learnings:
// If left to right traversal doesn't guaranteee a solution, try reverse

int maxProduct(vector<int>& nums) {
	int curMax = INT_MIN;
	int prod = 1;

	for (int i = 0 ; i < nums.size(); i++){
		prod*=nums[i];
		curMax=max(prod,curMax);
		if (prod==0){
		   	prod = 1; 
		}
	}

	prod = 1;
	for (int i = nums.size()-1 ; i >= 0; i--){
		prod*=nums[i];
		curMax=max(prod,curMax);
		if (prod==0) {
			prod = 1;
		}
	}
	cout << curMax;
	return curMax;
}


int main() {
	vector<int> x = { 1,2,3,-5,-2 } ;
	cout << "YOYOYO";
	return 0;
}
