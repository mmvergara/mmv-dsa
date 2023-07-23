#include <iostream>
#include <vector>
#include <Windows.h>
using namespace std;

class Game {
	private:

		bool XsTurn = true;
		vector<vector<string>> gameState = {
			{"-","-","-"},
			{"-","-","-"},
			{"-","-","-"},
		};

	public:

		void start(){
			XsTurn = true;
			gameState = {
			{"-","-","-"},
			{"-","-","-"},
			{"-","-","-"},
			};
			Turn();
		};



		void restart(){
		
		}

		void checkState(){
			// Check if someone won
			vector<string> flattenedState = Flatten(gameState);

			bool Xwon = checkPlayerWon(flattenedState,"X");
			bool Owon = checkPlayerWon(flattenedState,"O");
			bool isDraw = checkDraw(flattenedState);

			if (Xwon){
				WonDrawState("X");
			} else if (Owon){
				WonDrawState("O");
			} else if (isDraw){
				WonDrawState("D");
			} else {
				Turn();
			};
		}

		void WonDrawState(string x){
			system("cls");
			printState();
			if (x == "D"){
				cout << "=== DRAW !!! ===\n";
				cout << "press x if you want to continue\n";
			} else {
				cout << "=== " << x << " Won !!! ===\n";
				cout << "enter x if you want to continue: ";
			}
			string y;
			cin >> y;
			if (y == "x"){
				start();
			}
		}

		bool checkDraw(vector<string> flattenedState){
			bool draw = true;

			for (int i = 0 ; i < flattenedState.size() ; i++){
				if (flattenedState[i] == "-"){
					draw = false;
				}
			}
			return draw;
		}

		bool checkPlayerWon(vector<string> flattenedState, string player){
			vector<vector<int>> winningConditions = {
				{0,1,2},
				{3,4,5},
				{6,7,8},

				{0,4,8},
				{2,4,6},
				
				{0,3,6},
				{1,4,7},
				{2,5,8}
			};
			bool res = false;
			for (int i = 0; i < winningConditions.size();i++){
				if (res == true){
					break;
				}
				bool won = true;
				for (int j = 0; j < winningConditions[i].size(); j++){
					if (flattenedState[winningConditions[i][j]] != player){
						won = false;
					}
				};
				if (won == true) {
					res = won;
				};
			};
			return res;

		}

		vector<string> Flatten(vector<vector<string>>){
			vector<string> out = {};
			for (int i = 0; i < gameState.size(); i++){
				for (int j = 0 ; j < gameState[i].size(); j++){
					out.push_back(gameState[i][j]);
				};
			};
			return out;
		}

		void Turn() {
			int indexTurn;
			system("cls");
			printState();
			cout << "Select index 1-9 to occupy: ";
			cin >> indexTurn;
			int row = 0;
			if (indexTurn > 6){
				row = 2;
				indexTurn -= 6;
			} else if (indexTurn > 3){
				row = 1;
				indexTurn -= 3;
			};
			indexTurn--;
			if (gameState[row][indexTurn] != "-"){
				cout << "That space is already occupied \n";
				Turn();
				return;
			}

			if (XsTurn) {
				gameState[row][indexTurn] = "X";
				XsTurn = false;
			} else {
				gameState[row][indexTurn] = "O";
				XsTurn = true;
			};

			checkState();


				
		}

		void printState(){
			if (XsTurn) {
				cout << "X's turn\n";
			} else {
				cout << "O's turn\n";
			}

			for (int i = 0; i < gameState.size(); i++){
				cout << "\n";
				cout << "[";
				for (int j = 0; j < gameState[i].size();j++){
					cout << " " << gameState[i][j];
				}
				cout << " ]";
			}
			cout << "\n";
		};




	};


int main() {

	cout << "Hello";

	Game yo;
	yo.start();

	return 0;
}
