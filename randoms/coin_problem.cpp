#include <iostream>
#include <vector>

using namespace std;

int main(){

	vector<int> coins = {200,100,50,20,10,5,2,1};
	int target = 520;
	int x = 0;
	for ( size_t i = 0; i < coins.size(); i++) {
		while ( x < target ) {
			cout << x << endl;
			x+=coins[i];
			if ( x == target ) {
				cout << "TOTAL COINS: " << i+1 << "\n";
				break;
			}
		}
		if ( x > target ) {
			x-=coins[i];
		}
	}
	return 0;
}



