#include <iostream>
#include <vector>
using namespace std;

void printBoxes(vector<int> p1b ,vector<int> p2b){

	vector<string> pb = {"=","=","=","=","=","=","=","=","="};

	for (int i = 0 ; i < p1b.size(); i++){
		pb[p1b[i]] = "X";
	};

	for (int i = 0 ; i < p2b.size(); i++){
		pb[p2b[i]] = "O";
	};

	cout << "[ " << pb[0] << " " << pb[1] << " " << pb[2] << " ]\n";
	cout << "[ " << pb[3] << " " << pb[4] << " " << pb[5] << " ]\n";
	cout << "[ " << pb[6] << " " << pb[7] << " " << pb[8] << " ]\n";
	
}

bool inputTurn(bool P1Turn, int spot,vector<int> p1b ,vector<int> p2b){

	// check if that spot is available
	for ( int i : p1b ) {
		if ( i == spot) {
			return false;
		}
	};

	for ( int i : p2b) {
		if ( i == spot ) {
			return false;
		}
	}

	// add the string
	string sym = "O";
	if (P1Turn) {
		sym = "X";
		p1b.push_back(spot);
	} else {
		p2b.push_back(spot);
	}

	return true;




}

int main() {
	bool run = true;

	vector<vector<int>> winningConditions = {
		
		{0,1,2},
		{3,4,5},
		{6,7,8},

		{0,3,6},
		{1,4,7},
		{2,5,8},

		{0,4,8},
		{2,4,6},

	};

	bool P1Turn = true;
	vector<int> P1Boxes = {};
	vector<int> P2Boxes = {};


	
	printBoxes(P1Boxes,P2Boxes);
	while (run) {

		while (true) {
				
			if inputTurn()
		}
			break;


	}

	return 0;
}
