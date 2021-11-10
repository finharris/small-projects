#include <iostream>
using namespace std;
/*
if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
else (it is a leap year)
*/

int main() {
  int year;
  cout << "Enter a year to check if it is a leap year:" << endl;
  cin >> year;

  if (year > 999 && year < 10001) {
    // check is leap year
    if (year % 4 == 0 && year % 100 == 0 && year % 400 == 0) {
    cout << "This is a leap year." << endl;
    } else {
    cout << "This is not a leap year." << endl;
    }
  }
}