#include <iostream>
#include <vector>
#include <algorithm>

void permutation(int n) {
  // 1부터 n까지의 숫자를 저장하는 벡터 생성
  std::vector<int> numbers;
  for (int i=1; i<=n; ++i) {
    numbers.push_back(i);
  }

  do {
    for (int num : numbers) {
      std::cout << num;
    }
    std::cout << " ";
  } while (std::next_permutation(numbers.begin(), numbers.end()));

  std::cout << std::endl;
}

int main() {
  int n;
  std::cout << "n의 값을 입력하세요:";
  std::cin >> n;

  permutation(n);
}

