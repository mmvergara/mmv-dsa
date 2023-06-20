#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<int, int> cache;

int tribonacci(int n){
	if (n <= 0){
		return 0;
	}
	if (n == 1){
		return 1;
	}

	if (cache.find(n) != cache.end()){
		return cache[n];
	}

	int res = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
	cache[n] = res;
	return res;

} 

int main() {
	cout << tribonacci(25);
}
