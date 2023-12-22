"""
https://www.acmicpc.net/problem/1978
"""


def try1():
    """
    - 약 5분 소요
    - 소수 판별 함수는 암기해놓기 (시간복잡도 축소한 버전)
        - +1 까먹지말 것
        - 1 예외처리도 필요함
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    def is_prime_number(x):
        if x == 1:
            return 0
        for i in range(2, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                return 0
        return 1

    ans = 0
    for num in numbers:
        ans += is_prime_number(num)

    print(ans)


if __name__ == "__main__":
    try1()
