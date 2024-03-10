"""
https://www.acmicpc.net/problem/1010
"""


def try1():
    """
    - 약 12분 소요
    - 조합을 이용한 풀이
    - DP로도 풀이 가능하다고는 하지만 조합을 이용한 풀이가 직관적이라 판단됨
    """
    import sys
    from math import factorial as f

    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        ans = f(m) / (f(m - n) * f(n))

        print(int(ans))


def try2():
    """
    - 약 5분 소요
    - 강 서쪽은 무조건 다 선택되게 되어 있음 (N <= M 이므로)
    - 즉 강 동쪽의 사이트 중 서쪽의 개수만큼 연결시킬 사이트를 고르는 것과 동치
        - combination : mCn
    """
    import sys
    import math

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        print(int(math.factorial(m) / (math.factorial(m - n) * math.factorial(n))))


if __name__ == "__main__":
    # try1()
    try2()
