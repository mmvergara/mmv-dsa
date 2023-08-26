
#include <iostream>
using namespace std;

int main() {
	
	int result[3][3] = {
    	{1, 1, 1},
    	{1, 1, 1},
    	{1, 1, 1}
	};

	for (int r = 0; r < 3 ; r++){
		for (int c = 0; c < 3; c++){
			int n;
			cin >> n;

			if ( n % 2 != 0){

				// flip switches
				result[r][c] ^= 1;
				// vertical adjacents
				if ( (r+1) < 3 ) result[r+1][c] ^=  1;
				if ( (r-1) >= 0 ) result[r-1][c] ^=  1;
				
				// horizontal adjacents
				if ( (c+1) < 3 ) result[r][c+1] ^= 1;
				if ( (c-1) >= 0 ) result[r][c-1] ^= 1;
			
			}
		}
	}

	for (int r = 0; r < 3 ; r++){
		for (int c = 0 ; c < 3; c++){
			cout << result[r][c];
		}
		cout << "\n";
	}

    return 0;
}
