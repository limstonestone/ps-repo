"""
https://www.acmicpc.net/problem/2579
"""


def try1():
    """
    - 약 50분 풀이 후 실패로 답지 참조
    - 반복되는 연산 및 저장된 값을 활용하여 최적의 해 풀이 -> DP
    - DP 테이블의 값은 현재 위치까지의 최대값

    - 답지 풀이
        - 마지막 계단을 반드시 밟아야하므로 역으로 내려왔다고 생각하는 것이 좋음
        - 본인은 상태 변수를 선언하여 직전칸에서 올라온 횟수를 3번까지 제한했는데, 점화식 자체에 녹여버릴 수 있었음
            - 왜냐하면 직전 칸에서 올라온 경우의 최대값은 오른쪽을 현재칸이라고 가정했을 때, 아래와 같기 때문
                - OXOO (가장 오른쪽이 현재 칸, O/X는 방문 여부)

    """

    import sys

    input = sys.stdin.readline

    n = int(input())

    # 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
    stairs = [0] * 301
    for i in range(1, n + 1):
        stairs[i] = int(input())

    # dp 배열을 초기화합니다.
    dp = [0] * 301
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    # 점화식을 계산합니다.
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[n])


if __name__ == "__main__":
    try1()
