#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;


int minEatingSpeed(vector<int>& piles, int h) {
	// k = eating speed
	// we need to get the minimum eating speed to finish all piles within h hour
	

	int l = 1;
	int r = *max_element(piles.begin(),piles.end());
	int res = r;
	
	while ( l <= r ){
		int k = (l+r) / 2;
		int htta = 0;

		for (int i = 0 ; i < piles.size(); i++){
			htta += ceil(piles[i]/static_cast<double>(k));
		}

		if (htta <= h){
			res = min(res,k);
			r = k - 1;
		} else {
			l = k + 1;
		}

	}
    

	return res;
}

int main() {

	vector<int> inp1 = {30,11,23,4,20};
	int h = 5;
	
	int res = minEatingSpeed(inp1,h);
	cout << "=" << res << "=\n";
		
	return 0;
}
