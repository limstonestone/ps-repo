"""
https://www.acmicpc.net/problem/1026
"""


def try1():
    """
    - 약 5분 소요
    - B를 재배열 하면 안된다는 조건이 의미가 없음
        - A를 재배열하는 순간 어차피 순서에 대한 개념이 없어지기 때문
    - B의 가장 큰수에 A의 가장 작은 수를 곱해주면 최소값 완성 -> 그리디
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)

    s = 0
    for a, b in zip(A, B):
        s += a * b

    print(s)


if __name__ == "__main__":
    try1()
