#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two positive integers: ";
    cin >> a >> b;
    // 유클리드 알고리즘을 사용한 GCD 계산
    while (b != 0) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }
        int r = a % b;
        a = b;
        b = r;
    }
    cout << "The GCD is: " << a << endl;
    return 0;
}
