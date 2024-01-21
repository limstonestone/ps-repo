"""
https://www.acmicpc.net/problem/2407
"""


def try1():
    """
    - 약 15분 소요
    - 파스칼 삼각형 공식 : nCm = n-1Cm-1 + n-1Cm
        - 점화식 존재 + 이전 연산의 값 활용 -> DP
    - 간단하게 math 라이브러리의 factorial 함수를 사용해도 무방하긴 함
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    dp = [[1 for i in range(100 + 1)] for j in range(100 + 1)]

    for i in range(2, n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                continue
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print(dp[n][m])


if __name__ == "__main__":
    try1()
