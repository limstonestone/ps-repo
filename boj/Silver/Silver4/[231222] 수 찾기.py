"""
https://www.acmicpc.net/problem/1920
"""


def try1():
    """
    - 약 2분 소요
    - set 자료형을 활용하면 in 연산이 O(1)로 가능
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    A = set(list(map(int, input().split())))

    m = int(input())
    seq_m = list(map(int, input().split()))

    for i in range(m):
        print(1 if seq_m[i] in A else 0)


if __name__ == "__main__":
    try1()
