"""
https://www.acmicpc.net/problem/17219
"""


def try1():
    """
    - 약 4분 소요
    - 딕셔너리의 key value 활용 문제
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    pw2dict = dict()

    for _ in range(n):
        site, pw = input().split()
        pw2dict[site] = pw

    for _ in range(m):
        site = input().rstrip()
        print(pw2dict[site])


if __name__ == "__main__":
    try1()
