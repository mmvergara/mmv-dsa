
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int n;
	vector<int> nums;

	cin >> n;

	for (int i = 0; i < n; i++){
		int x;
		cin >> x;
		nums.push_back(x);
	}

	sort(nums.begin(),nums.end());

	for (int i = 0 ; i<n; i++){
		cout << nums[i] << " ";
	}

    return 0;
}
