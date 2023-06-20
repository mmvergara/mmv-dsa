#include <iostream>
#include <vector>
using namespace std;

void pvec (vector<int>& vec){
	cout << "{ ";
	for(int i = 0; i < vec.size(); i++)
    cout << vec[i] << ' ';
	cout << "}\n";
}

int minCostClimbingStairs(vector<int>& cost) {	
	
	
	for (int i = cost.size()-1; i>=0;i--){
		if ( i+1 == cost.size() || i+2 == cost.size()){
			continue;
		}

		
		//  next val      next next val
		cout << cost[i+1] << " " << cost[i+2] << endl;

		int c = cost[i];
		int ostep = cost[i+1];
		int tstep = cost[i+2];

		if (ostep == tstep){
			cout << tstep << "=1=\n";
			
			c += cost[tstep];
		} else if (ostep < tstep) {
			cout << "=2=\n";
			c += ostep;
		} else {
			cout << "=3=\n";
			c += tstep;
		}
		cout << "RES=" << c << endl;
		cost[i] = c;
		
		pvec(cost);
	}

	if (cost[0] < cost[1]){
		return cost[0];
	} else {
		return cost[1];
	}
	
}

int main(){
	vector<int> cost = {0,0,1,1};
	int res = minCostClimbingStairs(cost);
	cout << res << endl;

}
