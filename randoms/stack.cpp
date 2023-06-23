#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <algorithm>
#include <unordered_map>
using namespace std;

template<typename T>

class MyStack {

	private:
		vector<T> data;

	public:

		bool isEmpty() {
			if (data.size() == 0){
				return true;
			}
			return false;
		}

		void push(const T& val){
			data.push_back(val);
		}
		
		T peek(){
			if (isEmpty()){
				throw runtime_error("Stack is freaking empty");
			}
			return data[data.size()-1];
		}

		T pop(){
			if (isEmpty()){
				throw runtime_error("Stack is freaking empty");
			}
			T el = data[data.size()-1];
			data.pop_back();
			return el;
		}
	};



int main(){
	MyStack<int> cs;

	cs.push(1);
	cout << cs.peek() << endl;
	cs.pop();
	cout << cs.peek() << endl;
	


	return 0;

}
