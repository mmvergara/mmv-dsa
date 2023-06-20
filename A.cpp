
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int gameWithCells(int r, int c){

	if (r % 2 != 0) r+=1;
	if (c % 2 != 0) c+=1;

	return (r/2) * (c/2);
	


}


int main(){
	int res = gameWithCells(2,2);
	cout << "\n\nres=" << res << endl;
	return 0;

}
