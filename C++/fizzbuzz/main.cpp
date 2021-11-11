#include <iostream>

using std::cin;
using std::cout;
using std::endl;

void fizzBuzz(int n) {
    for (int i = 1; i < n + 1; i++) {
        std::string output;

        if (i % 3 == 0) output += "Fizz";
        if (i % 5 == 0) output += "Buzz";
        if (output.size() < 1) output = std::to_string(i);

        cout << output << endl;
    }
}

int main() {
    fizzBuzz(15);
}
