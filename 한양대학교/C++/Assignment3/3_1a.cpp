#include <iostream>
#include <cctype>  // toupper, isalpha 함수를 사용하기 위해 포함

void count_chars(char text[]) {
  int counts[26] = {0};

  for (int i=0; text[i] != '\0'; ++i) {
    if (std::isalpha(text[i])) {
      char upperChar = std::toupper(text[i]);
      int index = upperChar - 'A';
      counts[index]++;
    }
  }

  for (int i=0; i<26; ++i) {
    char upper = 'A' + i;
    char lower = 'a' +i;
    std::cout << upper << ", " << lower << " : " << counts[i] << std::endl;
  }
}

int main() {
  char text[] = "Today is a nice day for having a little picnic.";
  count_chars(text);
}
