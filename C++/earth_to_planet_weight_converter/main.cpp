#include <iostream>
using namespace std;

int main() {
  cout << "What is your earth weight?" << endl;
  double weight;
  cin >> weight;
  
  cout << "Enter the planet number you want ot know your weight on:" << endl;
  cout << "1	Mercury, 2	Venus, 3	Mars, 4	Jupiter, 5	Saturn, 6	Uranus, 7	Neptune" << endl;
  int planetno;
  cin >> planetno;
  
  switch (planetno) {
    case 1:
      cout << (weight * 0.38);
      break;

    case 2:
      cout << (weight * 0.91);
      break;

    case 3:
      cout << (weight * 0.38);
      break;

    case 4:
      cout << (weight * 2.34);
      break;

    case 5:
      cout << (weight * 1.06);
      break;

    case 6:
      cout << (weight * 0.92);
      break;

    case 7:
      cout << (weight * 1.19);
      break;

    default:
     break;
  }

}