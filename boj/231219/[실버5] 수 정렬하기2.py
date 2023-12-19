"""
https://www.acmicpc.net/problem/2751
"""


def try1():
    """
    - 약 2분 소요
    - N이 백만 -> O(NlogN) ~ O(N)
        - 파이썬의 기본 정렬은 O(NlogN), 병합 정렬 + 삽입 정렬
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    num = [int(input()) for _ in range(n)]
    num.sort(reverse=False)

    for n in num:
        print(n)


if __name__ == "__main__":
    try1()
