#include <iostream>
using namespace std;

int main() {
    int number = 0;
    int sum = 0;
    // 반복문을 통해 숫자 입력받기
    do {
        cout << "Enter a number (0 to quit): ";
        cin >> number;
        // 누적합 계산
        sum += number;
        // 0이 아닌 경우 누적합 출력
        if (number != 0) {
            cout << "Cumulative sum: " << sum << endl;
        }
    } while (number != 0);  // 입력값이 0이 아니면 반복
    cout << "Program terminated." << endl;
    return 0;
}
