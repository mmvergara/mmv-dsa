#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> keyboards, vector<int> drives, int b){
	int res = -1;
	for (int kb = 0 ; kb < keyboards.size(); kb++){
		for (int d = 0; d < drives.size(); d++){
			int cSum = keyboards[kb] + drives[d];
			if (cSum == b){
				return cSum;
			}
			if (cSum <= b){
				res = max(res,cSum);
			}
		}
	}
	return res;
}


int main(){
	vector<int> a1 = {3,2,10};
	vector<int> a2 = {5,2,8};
	int res = solve(a1,a2,10);
	cout << res << endl;

	return 0;
}
