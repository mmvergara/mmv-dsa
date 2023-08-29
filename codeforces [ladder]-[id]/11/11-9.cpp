#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int n;
	cin >> n;

	if (n<10){
		cout << "NO";
		return 0;
	}

	while (n>9){
		if (n%10 != 4 && n%10 != 7){
			cout << "NO";
			return 0;
		}
		n = floor(n/10);
	}

	cout << "YES";
    return 0;
}
