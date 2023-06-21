
#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

  
int primeCount(long n) {
	vector<int> primes = {};

	for ( int i = 2 ; i <= n ; i++){
		if (i % 2 != 0){
			primes.push_back(i);
		}
	}

	for (const auto& el : primes){
		cout << el << endl;
	}

	return 0;
}

int main(){
	int res = primeCount(47);
	return 0;

}
