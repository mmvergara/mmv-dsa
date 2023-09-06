#include <iostream>
#include <vector>
#include <windows.h>
#include <unistd.h>
#include <string>

using namespace std;

void render(vector<vector<char>>& board){
	string out = "\n";
	for (int r = 0 ; r < board.size(); r++){
		for (int c = 0 ; c < board.size(); c++)
			out += board[r][c] + " ";
		row += "\n";

	}
	cout << out;
}

vector<vector<char>> evaluateBoard(vector<vector<char>>& board){

	vector<vector<int>> neighbors = {
		{-1,0},
		{-1,1},
		{0,1},
		{1,1},
		{1,0},
		{1,-1},
		{0,-1},
		{-1,-1}
	};
	int n = board.size();
	vector<vector<char>> newBoard = {};
	for ( int r = 0; r < n; r++ ){
		vector<char> newRow = {};
		for (int c = 0; c < n; c++){
			int neighborsCount = 0;

			for ( int i = 0;  i < neighbors.size(); i++){
				int newR = r + neighbors[i][0];
				int newC = c + neighbors[i][1];
				if ( newR >= 0 && newC >= 0 && newC < n && newR < n ){
					if (board[newR][newC] == '#'){
						neighborsCount++;
					}
				}
			}

			if (board[r][c] == '#'){
				// if alive
				if (neighborsCount >= 4 || neighborsCount <= 1){
					newRow.push_back('-');
					continue;
				}
				newRow.push_back('#');
			} else {
				// if unpopulated 
				if (neighborsCount == 3){
					newRow.push_back('#');
					continue;
				}
				newRow.push_back('-');
			}

		}
		newBoard.push_back(newRow);
	}
	return newBoard;
}

int main() {


	vector<vector<char>> board = {};
	int n = 50;
	for ( int r = 0 ; r < n; r++){
		vector<char> row = {};
		for (int c = 0 ; c < n; c++){
			row.push_back('-');
		}
		board.push_back(row);
	}
	
	// Pre allocate
	board[10][11] = '#';
	board[11][12] = '#';
	board[12][10] = '#';
	board[12][11] = '#';
	board[12][12] = '#';
	while(true){
	system("cls");
	render(board);
	board = evaluateBoard(board);
	sleep(0.3);
	}
	return 0;
}
