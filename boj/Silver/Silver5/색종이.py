"""
https://www.acmicpc.net/problem/2563
"""


def try1():
    """
    - 약 30분 소요
    - 가로세로 크기가 10인 것은 고정
    - 겹치는 부분을 찾아야함 -> 평행이동 또는 규칙을 찾는 것? 무리 ...
    - 그래프 탐색 문제처럼 좌표 방문 여부를 통해 아예 겹치는 부분을 고민할 부분에서 제외해버리는게 핵심
    """
    import sys

    input = sys.stdin.readline
    n = int(input())
    background = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(n):
        x, y = map(int, input().split())
        for n_x in range(x, x + 10):
            for n_y in range(y, y + 10):
                background[n_x][n_y] = 1

    ans = 0
    for i in range(100):
        ans += sum(background[i])

    print(ans)


if __name__ == "__main__":
    try1()
