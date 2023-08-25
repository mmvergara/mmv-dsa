#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int matrix[5][5];

    // Read the input matrix
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> matrix[i][j];
        }
    };

	// find the i j 
	int r;
	int c;

		for(int i = 0; i < 5; i++){
			for (int j = 0; j < 5; j++){
				if ( matrix[i][j] == 1 ) {
					r = i;
					c = j;
				}
			
			}
		}
	
	int moves = abs(2-r) + abs(2-c);
	cout << moves << "\n";

	return 0;

}
