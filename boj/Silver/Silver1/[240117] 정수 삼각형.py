"""
https://www.acmicpc.net/problem/1932
"""


def try1():
    """
    - 약 40분 소요
    - 이전 값의 결과를 저장하여 다음 스텝에서 사용 -> DP
    - 현재를 기준으로 생각해야 편리
        - 현재 스텝에서의 최대값은 자신을 결정하는 왼쪽, 오른쪽 중 가장 최대의 누적합 값 + 현재의 값
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    numbers = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        # 맨 왼쪽, 맨 오른쪽은 단순히 이전의 맨 왼쪽/오른쪽 값을 더해서 내려옴
        numbers[i][0] += numbers[i - 1][0]
        numbers[i][-1] += numbers[i - 1][-1]

        for j in range(1, len(numbers[i - 1])):
            numbers[i][j] += max(numbers[i - 1][j - 1], numbers[i - 1][j])

    print(max(numbers[n - 1]))


if __name__ == "__main__":
    try1()
