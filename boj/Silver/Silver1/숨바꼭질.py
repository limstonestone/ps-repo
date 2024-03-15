"""
https://www.acmicpc.net/problem/1697
"""


def try1():
    """
    - 약 1시간 소요
    - 입력 범위가 10만 -> O(NlogN)
    - 수빈이가 동생보다 앞에 있다면 계속 뒤로 걷기만 하는 것이 답
    - 과거의 연산 기록을 저장하고 있다가 다음 연산에서 사용 -> DP
    - 현재 위치가 짝수라면
        - 2배 순간이동 한 것과 이전 걸음에서 걸어온 것 중 최소 값 비교
        - 사실 2배 순간이동 한 것이 무조건 최소 거리지만, n 이전 값들을 고려해야하기 때문에 코드의 간결성을 위해 아래와 같이 표현
    - 현재 위치가 홀수라면
        - 2배 후 뒤로 가서 현재로 온 값과 이전 값에서 걸어온 것과 비교
    - 그래프(좌표)탐색 + 최단거리 임을 활용하여 BFS 로도 풀이 가능
    """
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    dp = [int(1e9)] * (100_000 + 1 + 1)
    j = n

    for i in range(n + 1):  # 뒤로 가는 경우 미리 계산
        dp[i] = j
        j -= 1

    for i in range(n + 1, 100_000 + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
        else:
            dp[i] = min(dp[(i + 1) // 2] + 2, dp[i - 1] + 1)

    print(dp[k])


if __name__ == "__main__":
    try1()
