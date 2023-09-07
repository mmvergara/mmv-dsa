#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int num = 2932;
	int ans = INT_MAX;
	for ( int m = 1 ; m < num; m*=10){
		int a = num % m;
		int b = num / m;
		cout << a << "-" << b << endl;
		int sum =  ( num % m ) + (num / m );
		cout << sum << endl;
		ans = min(ans,sum);
	}
	cout << ans;
	return 0;
}
