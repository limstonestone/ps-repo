"""
https://www.acmicpc.net/problem/11726
"""


def try1():
    """
    - 약 10분 소요
    - 2xn 를 채우는 타일링 경우의 수는?
        - 점화식을 세울 수 있음 (반복되는 연산)
        - 2x(n-1) + 2x(n-2) -> 여백이 1개인 경우와 여백이 2개인 경우
            - 여백이 2개일 때와 1개가 똑같은 경우는 여백2개에서 눕힌 타일을 세우면 1개인 경우와 겹치기 때문
        - 10,007 로 나눈 나머지 -> DP의 힌트가 될 수 있음
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    dp = [0] * (n + 2)  # n 이 1이 들어왔을 때 오류 방지
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 10007

    print(dp[n])


if __name__ == "__main__":
    try1()
