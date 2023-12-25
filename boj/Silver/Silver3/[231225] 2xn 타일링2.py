"""
https://www.acmicpc.net/problem/11727
"""


def try1():
    """
    - 약 4분 소요
    - 타일링 / 나머지 -> DP (2xN 타일링 문제 업그레이드 버전)
        - a_n = a_{n-1} + (a_{n-2}*2)
        - a_{n-2} 에 2를 곱하는 이유는 눕힌 타일2개와 2x2타일 하나로 채울 수 있기 때문 (곱의 법칙)
    """

    import sys

    input = sys.stdin.readline

    dp = [0] * (1000 + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, 1000 + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
        dp[i] %= 10007

    n = int(input())
    print(dp[n])


if __name__ == "__main__":
    try1()
