#include <iostream>
#include <string>
using namespace std;


int main(){

	int n , t;
	cin >> n >> t;
	string s;
	cin >> s;


	for ( int i = 0 ; i < t ; i++) {
		for (int j = 0 ; j < n -1 ; j++){
			// if we encounter BG swap them
			if (s[j] == 'B' && s[j+1] == 'G'){
				swap(s[j],s[j+1]);
				// skip the next cause we swapped with it
				j++;
			}
		}

	}
	cout << s << "\n";
	return 0; 
}
