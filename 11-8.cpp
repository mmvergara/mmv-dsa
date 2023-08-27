#include <iostream>
#include <string>
using namespace std;

int main() {
	string s;
	cin >> s;
	
	string out = "";
	for (float i = 0 ; i < s.size() ; i++){
		if ( i == 0 ) {
			out+= toupper(s[i]);
		} else {
			out+=s[i];
		}
	}
	cout << out;

    return 0;
}
