
#include <iostream>
#include <cctype>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;

    int uppercaseCount = 0;
    int lowercaseCount = 0;

    for (char c : input) {
        if (isupper(c)) {
            uppercaseCount++;
        } else if (islower(c)) {
            lowercaseCount++;
        }
    }

    string result; // Create a new string to store the result

    if (lowercaseCount >= uppercaseCount) {
        for (char c : input) result += tolower(c);
    } else {
        for (char c : input) result += toupper(c);
   }

	cout << result;
    return 0;
}
