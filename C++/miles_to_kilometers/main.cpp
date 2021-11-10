#include <iostream>
using namespace std;

int main() {
  // Add your code below  
  cout << "Enter a distance in miles to find out how far it will be in kilometers." << endl;

  double distancem;
  cin >> distancem;

  double distancek = distancem * 1.60934;

  cout << "The distance in kilomiters is " << distancek << "." << endl;
}