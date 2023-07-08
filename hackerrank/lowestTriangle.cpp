

#include <iostream>
#include <vector>
#include <cmath>



using namespace std;

int lowestTriangle(int base,int area){
	int h = 2*area/base;
	if ((h*base/2)<area) h++;
	return h;
}


int main(){
	int res = lowestTriangle(17,100);
	cout << res;
	return 0;
}
