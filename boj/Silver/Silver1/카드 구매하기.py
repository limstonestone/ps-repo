"""
https://www.acmicpc.net/problem/11052
"""


def try1():
    """
    - 약 30분 소요
    - Pi = i 개 카드를 사는데 드는 비용
    - N개 구매를 사는데 드는 최대 비용을 구해야 함
    - 백트래킹으로 풀이 -> 시간초과
    - P의 길이가 1만으로 길어보이지만 이는 함정임
        - 어차피 N개 구매해야하므로, P의 길이는 N의 길이인 1000 까지만 고려하면됨
        - 즉 입력길이가 O(N) 이므로 O(N^2) 풀이가 가능하다는 뜻
    - 따라서 DP풀이 가능
    - 예시) 카드를 4개 갖는 과정은 아래 중 가장 최대값임, 점화식 작성 가능
        - P[4] 고르기
        - 카드를 3개 골랐을 때 최대값 + P[1] 고르기
        - 카드를 2개 골랐을 때 최대값 + P[2] 고르기
        - 카드를 1개 골랐을 때 최대값 + P[3] 고르기
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    P = [0] + list(map(int, input().split()))

    dp = [0] * (n + 1)
    dp[1] = P[1]
    dp[2] = max(P[1] * 2, P[2])

    for i in range(3, n + 1):
        dp[i] = max([dp[i - j] + P[j] for j in range(i + 1)])

    print(dp[n])

    ### 백트래킹 풀이
    # len_p = len(P)

    # ans = 0
    # tmp_ans = 0

    # def dfs(tmp_n):
    #     nonlocal ans, tmp_ans
    #     if tmp_n == n:
    #         ans = max(ans, tmp_ans)
    #         return
    #     if tmp_n > n:
    #         return

    #     for i in range(1, len_p + 1):
    #         tmp_ans += P[i - 1]
    #         dfs(tmp_n + i)
    #         tmp_ans -= P[i - 1]

    # dfs(tmp_ans)
    # print(ans)


if __name__ == "__main__":
    try1()
