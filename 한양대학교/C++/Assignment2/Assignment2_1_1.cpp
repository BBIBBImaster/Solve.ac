#include <iostream>

// 팩토리얼을 계산하는 함수
unsigned long long factorial(int n) {
  unsigned long long result = 1;
  for (int i = 1; i <= n; ++i) {
    result *= i;
  }
  return result;
}

// 이항 계수를 계산하는 함수
unsigned long long binomialCoeffiecient(int n, int r) {
  if (r > n) return 0;
  unsigned long long numerator = factorial(n);
  unsigned long long denominator = factorial(r) * factorial(n-r);
  return numerator / denominator;
}

int main() {
  int n, r;

  // 사용자로부터 입력 받기
  std::cout << "n과 r을 입력하세요: ";
  std::cin >> n >> r;

  // 이항계수 출력
  std::cout << "C(" << n << "," << r << ") = " << binomialCoeffiecient(n,r);

  return 0;
}