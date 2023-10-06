#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <unordered_map>


using namespace std;

void changeNum (int *x){
	*x = 10;
}

int main() {
	int num = 1;
	changeNum(&num);
	cout << num;
	
	
	return 0;
}
