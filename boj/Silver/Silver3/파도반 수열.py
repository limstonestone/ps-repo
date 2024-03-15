"""
https://www.acmicpc.net/problem/9461
"""


def try1():
    """
    - 약 3분 소요
    - 1,1,1,2,2,3,4,5,7,9
        - a_n = a_{n-2} + a{n-3} -> DP
        - n 은 100이 최대
    """
    import sys

    input = sys.stdin.readline

    t = int(input())
    dp = [0] * (100 + 1)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, 100 + 1):
        dp[i] = dp[i - 2] + dp[i - 3]

    for _ in range(t):
        n = int(input())
        print(dp[n])


if __name__ == "__main__":
    try1()
