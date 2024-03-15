"""
https://www.acmicpc.net/problem/2869
"""


def try1():
    """
    - 약 20분 소요
    - 입력 범위가 굉장히 큼 -> 단순 반복문 구현으로는 힘들 것
        - 나눗셈으로 구현 가능
    """
    import sys

    input = sys.stdin.readline

    A, B, V = map(int, input().split())

    mok = (V - A) // (A - B)  # (V-A) : 첫 날에 올라간 것을 계산
    V -= (mok) * (A - B)  # 아래 반복문에서 반복되는 부분을 빼줌

    cur = 0
    while True:  # 남은 부분을 해당 로직으로 계산 (해당 코드 위 연산을 지워도 정답이지만, 시간초과)
        cur += A
        mok += 1
        if cur >= V:
            break
        cur -= B

    print(mok)


def solution():
    """
    - 더 나은 풀이
    - 올라가야 하는 거리 = V-B
    - 하루에 올라가는 거리 = A - B
    - 나머지가 있는 경우는 낮에 다 올라가지 못해서 미끄러졌다는 것
        - 따라서 올림 연산
    """
    import math

    A, B, V = map(int, input().split())
    day = (V - B) / (A - B)
    print(math.ceil(day))


if __name__ == "__main__":
    try1()
