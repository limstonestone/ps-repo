"""
https://www.acmicpc.net/problem/1629
"""


def try1():
    """
    - 약 20분 소요
    - 입력의 범위가 매우 큼 -> 간단한 로직으로 구현 불가
    - 분할정복을 이용한 고속 거듭제곱 알고리즘
        - 지수 법칙을 활용하여 거듭제곱의 시간복잡도를 감소할 수 있음
            - 2^4 = 2^2 * 2^2 = 2^(2+2)
            - 2^5 = 2^2 * 2^2 + 2 -> 홀수 일때는 한 번 더 곱해주기만 하면 됨
        - 기존 거듭제곱 방식의 시간복잡도는 O(N)
        - 고속 거듭제곱 알고리즘의 시간복잡도는 O(logN)
    """
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    def power(a, b):
        if b == 0:
            return 1

        x = power(a, b // 2)

        return (x * x) % c if b % 2 == 0 else (x * x * a) % c

    print(power(a, b))


if __name__ == "__main__":
    try1()
