"""
https://www.acmicpc.net/problem/9465
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 과거 값들을 저장해두었다가 재사용 -> DP
    - DP 테이블을 2행으로 만들어 해결
    - DP 테이블의 값은 각각 현재 스티커를 선택했을 때 최대치

    - 답지 풀이
        - 현재 값을 무조건 선택한다고 가정하면 DP테이블은 반대편만 고려하면 됨
        - 반대편만 고려하되, 이전에 선택했는지 선택안했는지만 고려!
            - 이렇게하면 양 테이블이 교차되면서 모든 경우를 계산할 수 있게 됨
    """
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0 for _ in range(n)] for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]

        if n == 1:
            print(max(dp[0][0], dp[1][0]))

        else:
            dp[0][1] = dp[1][0] + sticker[0][1]
            dp[1][1] = dp[0][0] + sticker[1][1]

            for i in range(2, n):
                dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + sticker[0][i]
                dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + sticker[1][i]

            print(max(dp[0][n - 1], dp[1][n - 1]))


if __name__ == "__main__":
    try1()
