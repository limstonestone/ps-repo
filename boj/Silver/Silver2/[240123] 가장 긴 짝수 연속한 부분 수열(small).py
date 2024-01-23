"""
https://www.acmicpc.net/problem/22857
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 과거 연산을 저장해두었다 활용 -> DP
    - 입력 범위가 5만이므로 시간복잡도에 주의해야함 -> O(N^2) 미만

    - 답지 풀이
        - 삭제 횟수를 DP 테이블의 차원으로 간주한 풀이
        - 왼쪽 / 오른쪽을 함께 생각하면 배반 사건이 안됨 -> 왼쪽으로만 생각 (과거 값만 생각)

    """
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    s = [0] + list(map(int, input().split()))
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    ans = 0

    for i in range(1, n + 1):
        s[i] %= 2  # S의 원소를 짝, 홀로 변환 (아래 조건문 표기를 편리하게 하기 위함)

        for j in range(k + 1):  # 삭제를 아예 안했을 때부터 최대 k 번 삭제했을 때 까지
            if not s[i]:  # 짝수라면 -> 삭제횟수 안 늘어남, 부분 수열 길이 늘어남
                dp[i][j] = dp[i - 1][j] + 1

            if j != 0 and s[i]:  # 홀수라면
                # j == 0 라면, 즉 삭제를 하지 않을 것이라면 홀 수일 때는 부분 수열에서 상관할 것이 아님
                # 왼쪽 원소의 값으로 이동(현재 값 삭제)한 후 삭제횟수를 하나 차감했다는 뜻
                dp[i][j] = dp[i - 1][j - 1]

        ans = max(ans, dp[i][k])  # 최대 k 번까지 돌았을 때의 값

    print(ans)


if __name__ == "__main__":
    try1()
