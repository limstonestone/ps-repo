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


if __name__ == "__main__":
    try1()
