# 1. 가방 오름차순 정렬
# 2. 보석 무게 오름차순 정렬
# 3. 보석 값 최대 힙
# ----------------
# 1. 가방 작은 순서대로 선택
# 2. 선택된 가방에 넣을 수 있는 모든 보석을 힙에 넣음
# 3. 가방에 넣을 수 있는 가장 비싼 보석을 선택


import sys

class gem:
    def __init__(self, m, v):
        self.m = m
        self.v = v


n, k = map(int, sys.stdin.readline().split())

