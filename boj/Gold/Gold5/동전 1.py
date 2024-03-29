"""
https://www.acmicpc.net/problem/2293
"""


def try1():
    """
    - 약 1시간 30분 풀이 후 실패로 답지 참조
    - 동작 원리를 보았을 때 DP인듯 함
        - 백트래킹은 시도는 해보았으나 순서를 고려하지 않는 로직을 구현 X
    - DP[k] = K원을 만들기위한 경우의 수
        - DP[i] += DP[i - c] for c in coin:
        - 이런 느낌으로 가는 것 같은데 ... 중첩되는 경우가 발생

    - 답지 풀이
        - 1, 2, 5가 주어졌다고 가정하자.
        - 1원을 썼을 때 1~k 원의 경우의 수를 1로 계산
        - 2원을 썼을 때 2원에 해당하는 배수만큼 계속 덮어씀
            - 4원을 썼을 때의 경우의 수 = 2원을 썼을 때 + 나머지를 1원으로 채우는 경우의 수
        - 5원을 썼을때도 마찬가지
        - 코드로 이해하는 것이 쉬울듯 함
    """
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    coin = [int(input()) for _ in range(n)]

    dp = [0] * (k + 1)
    dp[0] = 1  # dp[0] = dp[k-k], k원짜리 동전 하나만 사용하는 경우 <-중요

    for c in coin:
        for i in range(
            c, k + 1
        ):  # i-c가 음수가 되지 않도록 c부터 시작(애초에 4원 동전을 3원 만드는데 사용 불가)
            dp[i] += dp[i - c]  # i 에 동전하나 뺀만큼의 가격을 만드는 경우의 수

    print(dp[k])


if __name__ == "__main__":
    try1()
