"""
https://www.acmicpc.net/problem/1149
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 연산 결과를 기억해놓았다가 다시 활용하는 방식 -> DP
    - 우선 현재 주어진 스텝에서의 최선은 현재 주어진 비용 중 가장 작은 것을 선택하는 것
    - 또한 다음 선택은 오로지 이전 선택의 영향만을 받는다
        - 즉 첫 출발이 중요하다? -> 2차원 DP 테이블로 3개의 열 구성
    - 단순히 숫자로서 더해나가면 한 행에 같은 숫자가 있을 경우 위치 정보를 파악할 수 없게됨

    - 답지 참조
        - 첫 출발 관점이 아닌 현재가 R,G,B 인지에 따라 이전 값을 더해주면 앞서 말한 문제들 해결 가능
        - 즉 현재 값은 무조건 고정! 이전 값의 최솟값에 더해줌
    """
    import sys

    input = sys.stdin.readline
    n = int(input())

    cost = [0] + [list(map(int, input().split())) for _ in range(n)]
    dp = [[1e9 for _ in range(3)] for _ in range(n + 1)]

    for i in range(3):
        dp[1][i] = cost[1][i]

    for i in range(2, n + 1):
        dp[i][0] = (
            min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        )  # 이전 값이 2번째, 3번째인 것 중 최소 + 현재 값 (1번 째)
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]

    print(min(dp[n]))


def try2():
    """
    - 약 5분 소요
    - 과거의 연산 값을 기억해뒀다가 활용 -> DP
        - R,G,B 세가지 경우의 수 밖에 없으므로 2차원 DP 테이블 활용
    - 각 단계의 최소값은 현재 해당하는 색과 그것을을 제외한 이전 값의 최소의 합 -> 점화식 도출 가능
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    house = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        house[i][0] += min(house[i - 1][1], house[i - 1][2])  # R
        house[i][1] += min(house[i - 1][0], house[i - 1][2])  # G
        house[i][2] += min(house[i - 1][0], house[i - 1][1])  # B

    print(min(house[n - 1]))


if __name__ == "__main__":
    # try1()
    try2()
