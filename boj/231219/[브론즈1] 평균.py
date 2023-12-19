"""
https://www.acmicpc.net/problem/1546
"""


def try1():
    """
    - 약 3분 소요
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    scores = list(map(int, input().split()))
    m = max(scores)

    print(sum(scores) / m * 100 / n)


if __name__ == "__main__":
    try1()
