"""
https://www.acmicpc.net/problem/1003
"""


def try1():
    """
    - 약 20분 소요
    - 그냥 주어진대로 구현하면 시간 초과 발생 -> 반복되는 연산이므로 DP
        - DP 배열을 2차원으로 만든 후, 점화식을 그대로 옮겨서 사용
    """
    import sys

    input = sys.stdin.readline

    dp = [[-1, -1] for _ in range(41)]  # n이 최대 40

    dp[0][0], dp[0][1] = 1, 0
    dp[1][0], dp[1][1] = 0, 1

    for i in range(2, 41):
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]  # 0의 개수
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]  # 1의 개수

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*dp[n])


if __name__ == "__main__":
    try1()
