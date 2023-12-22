"""
https://www.acmicpc.net/problem/2178
"""


def try1():
    """
    - 약 20분 소요
    - 주어진 그래프를 조건에 맞게 탐색 + 최소 방문 -> BFS
        - DFS 는 깊이를 우선적으로 탐색하므로 최단 경로를 보장하지 않음
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    visited = []
    for _ in range(n):
        graph.append(list(input().rstrip()))
        visited.append([0] * m)

    queue = deque([(0, 0)])
    visited[0][0] = 1

    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if (0 <= nx <= n - 1) & (0 <= ny <= m - 1):
                if (not visited[nx][ny]) & (graph[nx][ny] != "0"):
                    queue.append((nx, ny))
                    visited[nx][ny] += visited[x][y] + 1

    print(visited[n - 1][m - 1])


if __name__ == "__main__":
    try1()
