"""
https://www.acmicpc.net/problem/11660
"""


def try1():
    """
    - 약 50분 소요
    - 이미 계산한 누적합의 경우 또 다시 탐색할 필요가 없음
        - 과거 계산해놓은 값을 활용 -> DP
    - M의 길이가 10만이므로 단순 구현으로는 시간초과
        - DP로 누적합을 먼저 구한다음, 겹치는 부분들을 빼는 식으로 구현

    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())

    dp = [list(map(int, input().split())) for _ in range(n)]

    # 세로 누적합 만들기
    for y in range(n):
        for x in range(1, n):
            dp[x][y] += dp[x - 1][y]

    # 가로 누적합 만들기
    for x in range(n):
        for y in range(1, n):
            dp[x][y] += dp[x][y - 1]

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        ans = dp[x2 - 1][y2 - 1]

        if x1 > 1:
            ans -= dp[x1 - 2][y2 - 1]  # 세로로 긴 사각형 뺌
        if y1 > 1:
            ans -= dp[x2 - 1][y1 - 2]  # 가로로 긴 사각형 뺌
        if x1 > 1 and y1 > 1:  # 중복으로 뺀 부분 다시 합쳐줌
            ans += dp[x1 - 2][y1 - 2]

        print(ans)


if __name__ == "__main__":
    try1()
