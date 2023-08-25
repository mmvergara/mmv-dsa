
#include <string>
#include <iostream>

using namespace std;

int main() {
	string c;
	cin >> c;

	string out;

	for (size_t i = 0 ; i < c.size(); i++){
			
		if (c[i] == '-' && c[i+1] == '-'){
			out += '2';
			i++;
			continue;
		}

		if (c[i] == '-' && c[i+1] == '.'){
			out += '1';
			i++;
			continue;
		}
		if (c[i] == '.'){
			out += '0';
		}
	}

	cout << out << "\n";

    return 0;
}
