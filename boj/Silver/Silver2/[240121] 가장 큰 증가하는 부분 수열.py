"""
https://www.acmicpc.net/problem/11055
"""


def try1():
    """
    - 약 5분 소요
    - 과거 연산 값을 참고하여 현재 값 계산 -> DP
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    A = list(map(int, input().split()))
    dp = A.copy()

    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + A[i])

    print(max(dp))


if __name__ == "__main__":
    try1()
