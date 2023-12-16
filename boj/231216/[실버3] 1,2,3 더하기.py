"""
https://www.acmicpc.net/problem/9095
"""


def try1():
    """
    - 약 5분 소요
    - 반복되는 연산을 저장해두고 사용 -> DP
        - i - 1 = 1을 더해서 정답이 되는 경우
        - i - 2 = 2를 더해서 정답이 되는 경우
        - i - 3 = 3을 더해서 정답이 되는 경우
    """
    import sys

    input = sys.stdin.readline

    t = int(input())
    dp = [0] * (11 + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11 + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for _ in range(t):  # 정답 출력
        print(dp[int(input())])


if __name__ == "__main__":
    try1()
