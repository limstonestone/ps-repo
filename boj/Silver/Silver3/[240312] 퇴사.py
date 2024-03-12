"""
https://www.acmicpc.net/problem/14501
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - N이 15 이하로 매우 적음 -> 시간복잡도 상관 X
        - 이중 반복문(O(N^2))을 고려해도 상관없음
    - 현재의 최선값을 과거값을 통해 구함 -> DP

    - 답지 풀이
        - 상담이 가능한 모든 날짜를 탐색하여 상담을 진행했을 때 얻는 최대 수익을 dp 테이블에 저장
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    seq = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)

    for i in range(n):
        t, p = seq[i]
        for j in range(i + t, n + 1):  # 현재 일자에 상담을 진행했다면 어떨지 탐색
            if dp[j] < dp[i] + p:  # 현재 일자에 상담을 진행했을 때 값이 더 크다면
                dp[j] = dp[i] + p  # 미래의 값은 현재 상담을 진행했을 때의 값으로 갱신

    print(dp[n])


if __name__ == "__main__":
    try1()
