"""
https://www.acmicpc.net/problem/10026
"""


def try1():
    """
    - 약 15분 소요
    - 그래프 탐색 문제
    - 가장 쉬운 접근으로 그래프를 두 개 만들어 메모리를 더 사용하고 시간복잡도를 줄이는 풀이
    - 재귀 깊이에 대해 주의하기
    """

    import sys

    sys.setrecursionlimit(int(1e9))

    input = sys.stdin.readline

    n = int(input())
    graph = []
    graph_yes = []  # 적록색약
    for i in range(n):
        tmp_input = list(input().rstrip())
        graph.append(tmp_input)
        tmp_yes_input = []

        for x in tmp_input:
            x = "R" if x == "G" else x
            tmp_yes_input.append(x)

        graph_yes.append(tmp_yes_input)

    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    ans, ans_yes = 0, 0

    def dfs(graph, x, y, value):
        graph[x][y] = "X"

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) & (0 <= ny < n):
                if (graph[nx][ny] != "X") & (graph[nx][ny] == value):
                    dfs(graph, nx, ny, value)

    for x in range(n):
        for y in range(n):
            if not graph[x][y] == "X":
                dfs(graph, x, y, graph[x][y])
                ans += 1
            if not graph_yes[x][y] == "X":
                dfs(graph_yes, x, y, graph_yes[x][y])
                ans_yes += 1

    print(ans, ans_yes)


if __name__ == "__main__":
    try1()
