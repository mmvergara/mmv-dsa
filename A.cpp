#include <iostream>
#include <vector>

std::vector<int> subset;
int n;

void processSubset() {
    // Print the subset
    std::cout << "{ ";
    for (int element : subset) {
        std::cout << element << "";
    }
    std::cout << "}\n";
}

void search(int k) {
    if (k == n) {
        processSubset();
    } else {
        search(k + 1);
        subset.push_back(k);
        search(k + 1);
        subset.pop_back();
    }
}

int main() {
    std::cout << "Enter the value of n: ";
    std::cin >> n;

    search(0);

    return 0;
}
