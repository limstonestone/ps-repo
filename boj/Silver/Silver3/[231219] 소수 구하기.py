"""
https://www.acmicpc.net/problem/1929
"""


def try1():
    """
    - 약 5분 소요
    - 에라토스테네스의 체 없이도 풀리긴 하지만 전형적인 문제
    """

    import sys

    input = sys.stdin.readline

    m, n = map(int, input().split())

    for num in range(m, n + 1):
        status = True
        if num != 1:
            for i in range(2, int(num ** (1 / 2)) + 1):
                if num % i == 0:
                    status = False
                    break
            if status:
                print(num)


if __name__ == "__main__":
    try1()
