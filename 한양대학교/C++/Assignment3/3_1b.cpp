#include <iostream>
#include <cctype>  // toupper, isalpha 사용을 위해 필요
#include <algorithm>  // std::max 사용을 위해 필요

void count_chars(char text[]) {
    int counts[26] = {0};  // A-Z의 발생 횟수를 저장하는 배열

    // 문자 발생 횟수 세기
    for (int i = 0; text[i] != '\0'; ++i) {
        if (std::isalpha(text[i])) {
            char upperChar = std::toupper(text[i]);
            int index = upperChar - 'A';
            counts[index]++;
        }
    }

    // 최대 발생 횟수를 찾기 (바 차트의 높이를 결정하기 위해)
    int max_count = *std::max_element(counts, counts + 26);

    // 바 차트 출력
    for (int i = max_count; i > 0; --i) {
        for (int j = 0; j < 26; ++j) {
            if (counts[j] >= i) {
                std::cout << "* ";  // 문자의 발생 횟수만큼 '*' 출력
            } else {
                std::cout << "  ";  // 발생 횟수가 부족하면 공백 출력
            }
        }
        std::cout << std::endl;  // 한 줄 끝나면 줄바꿈
    }

    // 알파벳 출력 (A-Z)
    for (char c = 'A'; c <= 'Z'; ++c) {
        std::cout << c << " ";
    }
    std::cout << std::endl;
}

int main() {
    char text[] = "Today is a nice day for having a little picnic.";
    count_chars(text);
    return 0;
}
