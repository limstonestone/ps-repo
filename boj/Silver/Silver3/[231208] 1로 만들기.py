"""
https://www.acmicpc.net/problem/1463
"""


def try1():
    """
    - 약 47분 소요
    - 최소한의 연산으로 1을 만드려면 큰 수로 최대한 나누는것이 중요 -> 그리디
        - 인줄 알았으나 반례를 여러개 만들어보면 꼭 3으로 최대한 나누는게 좋은 것이 아님
        - 구하고자 하는 값(최소 연산 횟수)에 대한 점화식을 세울 수 있음
    - 최소 연산 횟수를 dp 테이블의 값으로 설정 -> dp 로 풀이 가능
        - 결국 나누어 떨어진다면 미리 저장해둔 그 값의 최소 연산 횟수 + 1(나눈 연산) 이기 때문에 DP로 접근할 수 있는 것
        - 그 과정에서 1을 뺀 만큼만 더해주면 됨
        - N의 범위가 굉장히 큰것이 힌트일 수 있음
    - 개인적으로 DP는 아직 많이 낯설다, 연습 필수!
    """

    N = int(input())
    n = N + 3  # N=1(최솟값)이 주어지더라도 반복문에서 오류가 나지 않도록
    dp = [0] * (n)
    dp[1], dp[2], dp[3] = 0, 1, 1  # dp[1] = 0 값을 주지 않으면 틀림

    for i in range(4, n):
        remain3 = i % 3
        remain2 = i % 2
        dp[i] = min(
            dp[int((i - remain3) / 3)] + 1 + remain3,
            dp[int((i - remain2) / 2)] + 1 + remain2,
        )

    print(dp[N])


if __name__ == "__main__":
    try1()

# 17 -> 17-1, 16/2, 8/2, 4/2, 2/1
