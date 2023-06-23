
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int closestNumber(int a, int b, int x) {


	double p = pow(a,b);

	int i = 1;
	int lastX = x;
	int curX = x;
	if ( p < curX ) {
		// going backwards
		while (p < curX){
			lastX = curX;
			curX -= x;
		}
	} else {
		// going forward
		while (p > curX) {
			lastX = curX;
			curX += x;
		}
	}
	double lx = abs(p - lastX);
	double cx = abs(p - curX);
	


	cout << "LX=" << lx << "CX=" << cx << endl;
	if ( lx < cx ) {
		return lastX;
	} else {
		return curX;
	}
}


int main(){
	int res = closestNumber(395,1,7);
	return 0;

}
