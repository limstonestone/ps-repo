"""
https://www.acmicpc.net/problem/7562
"""


def try1():
    """
    - 약 14분 소요
    - 최단경로 탐색 -> BFS
    """
    import sys
    from collections import deque
    from itertools import product

    input = sys.stdin.readline

    t = int(input())
    direction = [
        (a * x, b * y)
        for a, b in [(2, 1), (1, 2)]
        for x, y in product([1, -1], repeat=2)
    ]  # 체스의 움직임

    def bfs(graph, x, y):
        q = deque([[x, y]])

        if (x, y) == (end_x, end_y):  # 시작부터 똑같으면 바로 0 리턴
            return 0

        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (0 <= nx < l) and (0 <= ny < l) and (graph[nx][ny] == 0):
                    q.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1
                    if (nx, ny) == (end_x, end_y):
                        return graph[nx][ny]

    for _ in range(t):
        l = int(input())
        graph = [[0 for _ in range(l)] for _ in range(l)]

        start_x, start_y = map(int, input().split())
        end_x, end_y = map(int, input().split())

        print(bfs(graph, start_x, start_y))


if __name__ == "__main__":
    try1()
