"""
https://www.acmicpc.net/problem/7576
"""


def try1():
    """
    - 약 30분 소요
    - 그래프 탐색 문제
        - 여러 시작점에서 동시에 시작 -> BFS
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    m, n = map(int, input().split())
    ans_zero = True
    graph = []
    start = []

    for x in range(n):
        tmp_tomato = list(map(int, input().split()))
        tomato = []

        for y in range(m):
            if tmp_tomato[y] == 0:
                ans_zero = False
            if tmp_tomato[y] == 1:
                start.append((x, y))

            tomato.append(tmp_tomato[y])

        graph.append(tomato)

    def bfs(graph, start):
        q = deque(start)
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n) & (0 <= ny < m):
                    if graph[nx][ny] == 0:
                        q.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1

        return graph

    if ans_zero:
        print(0)

    else:
        graph = bfs(graph, start)
        ans = 0
        for g in graph:
            if 0 in g:
                ans = 0
                break
            ans = max(ans, max(g))

        print(ans - 1)  # 처음 시작이 1이므로 1이 빠져야 정상


if __name__ == "__main__":
    try1()
