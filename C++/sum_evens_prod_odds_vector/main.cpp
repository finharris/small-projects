#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> nums = {2, 4, 3, 6, 1, 9};

  int evens = 0, oddp = 1;

  for (int i = 0; i < nums.size(); i++){
    int cur = nums[i];
    
    if (cur % 2 == 0) {
      // even
      evens += cur;
    } else {
      oddp *= cur;
    }
  }

  cout << "Sum of even numbers is " << evens << endl;
  cout << "Product of odd numbers is " << oddp << endl;
}