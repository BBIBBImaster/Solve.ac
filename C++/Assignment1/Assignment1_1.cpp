#include <iostream>
using namespace std;

int main() {
    int num1, num2, num3;
    // 1. Read three integer values using cin
    cout << "Enter three integers: ";
    cin >> num1 >> num2 >> num3;
    // 2. Determine the maximum of the three values
    int max_val = num1; 
    if (num2 > max_val) {
        max_val = num2;
    }
    if (num3 > max_val) {
        max_val = num3;
    }
    // 3. Print the maximum value using cout
    cout << "The maximum value is: " << max_val << endl;
    return 0;
}
