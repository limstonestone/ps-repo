"""
https://www.acmicpc.net/problem/2156
"""


def try1():
    """
    - 약 40분 소요
    - 과거 연산을 저장해서 다음 결과에 반영 -> DP
    - 경우의 수를 잘 분할하는 것이 중요, 그렇지 않으면 겹치는 사건 발생 (교집합 없이!)
    - dp[i - 2] + wine[i] : 이전 와인을 선택하지 않음 + 현재 와인 선택
    - dp[i - 3] + wine[i - 1] + wine[i] : 이전 와인을 선택함 + 현재 와인 선택
    - dp[i - 1] : 현재 와인을 선택하지 않았을 때의 가장 큰 정답 값 (갈수록 같거나 커지므로)
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    wine = [int(input()) for _ in range(n)] + [0] * 2  # 인덱싱 에러 방지용
    dp = [0 for _ in range(n + 2)]
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1])

    print(dp[n - 1])


if __name__ == "__main__":
    try1()
