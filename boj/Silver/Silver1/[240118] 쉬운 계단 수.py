"""
https://www.acmicpc.net/problem/10844
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 맨 뒷자리가 0, 9이면 나올 수 있는 경우의 수는 1
    - 이외에는 2개 (-> *2)
    - 이를 어떻게 표현? 2차원 배열로 표현

    - 답지 풀이
        - *2 로 풀어내는 것이 아닌 앞에오는 숫자 -1, +1 로 합산
        - 0 처리도 같이 수행, 맨 앞에 0이 오는 경우를 배열 값을 0으로 하여 처리(dp[1][0]=0)
        - 맨 뒷자리에 집중하는 것이 아닌 맨 앞자리에 오는 숫자에 집중
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:  # 맨 앞 번호가 0 (만약 맨 처음이 0이면 값이 0이니 계산 X)
                dp[i][j] = dp[i - 1][1]
            elif j == 9:  # 맨 앞 번호가 9 -> 이전 값이 8일 때의 경우의 수
                dp[i][j] = dp[i - 1][8]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    print(sum(dp[n]) % 1_000_000_000)


def try2():
    """
    - 약 45분 소요
    - 계단 수는 결국 앞자리 수의 영향을 받음
        - 앞자리의 경우의 수 + 2
    - 이때 예외적으로 현재 자리가 9라면 앞에 8밖에 오지 못함
    - 또한 현재 자리가 0이라면 앞자리에 1밖에 오지 못함
    - 0과 9가 고정이므로 2차원 배열의 인덱스를 통해 가지를 뻗어나가는 식으로 구현
    """
    import sys

    input = sys.stdin.readline
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n + 1)]

    for j in range(1, 10):
        dp[1][j] += 1

    for i in range(2, n + 1):
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]

    print(sum(dp[n]) % 1_000_000_000)


if __name__ == "__main__":
    # try1()
    try2()
