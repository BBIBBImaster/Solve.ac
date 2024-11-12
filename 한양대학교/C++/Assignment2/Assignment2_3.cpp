int sum_down(int x) {
    int result = 1;  // 기저 조건인 x < 0일 때 반환 값
    while (x > 0) {
        x = x - 1;  // x 값을 1씩 줄임
        result = 2 * x + result;  // 결과 누적
    }
    return result;
}

