"""
https://www.acmicpc.net/problem/2839
"""


def try1():
    """
    - 약 15분 소요
    - N 최대 5천 -> O(NlogN) ~ O(N^2)
    - 반복되는 연산을 저장해놓으면 편리한 문제 -> DP
        - ex) 9에서 3을 뺄지, 5를 뺄지는 6과 4 두 가지 중 최소의 값을 갖는 숫자로 결정
    """

    import sys

    input = sys.stdin.readline

    n = int(input())

    dp = [1e9] * (n + 3)  # 3이 입력되더라도 인덱싱 오류가 나지 않도록
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3] + 1, dp[i - 5] + 1)

    print(dp[n] if dp[n] < 1e9 else -1)


if __name__ == "__main__":
    try1()
