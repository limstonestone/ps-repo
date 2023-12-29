"""
https://www.acmicpc.net/problem/21736
"""


def try1():
    """
    - 약 10분 소요
    - 그래프 탐색의 기본적인 문제, 시작점의 위치는 기억하고 있어야 함
    """
    import sys

    sys.setrecursionlimit(int(1e9))

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = []

    for i in range(n):
        location = list(input().strip())
        if "I" in location:
            j = location.index("I")
            start = (i, j)
        graph.append(location)

    visited = [[False for _ in range(m)] for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ans = 0

    def dfs(graph, visited, node):
        nonlocal ans
        x, y = node
        visited[x][y] = True

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) & (0 <= ny < m) and (graph[nx][ny] != "X"):
                if not visited[nx][ny]:
                    if graph[nx][ny] == "P":
                        ans += 1
                    dfs(graph, visited, (nx, ny))

    dfs(graph, visited, start)
    print(ans if ans != 0 else "TT")


if __name__ == "__main__":
    try1()
