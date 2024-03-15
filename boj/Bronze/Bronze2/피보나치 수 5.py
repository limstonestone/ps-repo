"""
https://www.acmicpc.net/problem/10870
"""


def try1():
    """
    - 약 1분 소요
    - 점화식이 명확하게 주어진 DP 문제
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    dp = [0 for _ in range(n + 3)]
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])


if __name__ == "__main__":
    try1()
