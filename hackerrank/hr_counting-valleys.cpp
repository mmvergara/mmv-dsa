#include <iostream>
#include <vector>

using namespace std;

int solve(int steps, string path){	
	vector<int> arr = {};
	int l = 0;
	int valleys = 0;
	for( int i = 0; i < path.length(); i++){
		char x = path.at(i);
		char u = 'U';
		if (x == u){
			l++;
		} else {
			l--;
		}
		
		if ( l == 0 && arr.at(arr.size()-1) < 0){
			cout << "FOUND VALLEY" << endl;
			valleys++;
		}
		arr.push_back(l);
		cout << x << endl;
	};

	return valleys;
}

int main(){
	int res = solve(8 ,"UDDDUDUU");
	cout << res << "\n";
	return 0 ;
}
