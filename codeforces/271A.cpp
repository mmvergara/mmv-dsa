#include <iostream>
#include <cmath>
#include <unordered_set>

using namespace std;

int main() {
	int n;
	cin >> n;
	
	for ( int i = n+1; i < 19000;i++){

		// check current year
		bool passed = true;
		int c = i;
		unordered_set<int> curNums;
		while ( c > 0 ) {
			int digit  = c % 10;
			if (curNums.count(digit) > 0){
				passed = false;
				break;
			}
			curNums.insert(digit);
			c = c / 10;
		}

		if (passed){
			cout << i << "\n";
			break;
		}
	}


    return 0;
}
