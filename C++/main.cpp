#include<iostream>
#include<math.h>

using std::cout;
using std::cin;
using std::endl;

int main() {
  //  Write a program in C++ to calculate the volume of a cube.

  int side;
  cout << "Enter the side of the cube: ";
  cin >> side;
  cout << "The volume of the cube is: " << pow(side, 3) << endl;
}