"""
https://www.acmicpc.net/problem/1012
"""


def try1():
    """
    - 약 15분 소요
    - 그래프 탐색 문제
    - 방문 배열을 만들 필요 없이 그래프 값 자체를 변경해주면 됨
    - 재귀로도 풀이 가능
    """
    import sys

    input = sys.stdin.readline

    t = int(input())

    def dfs(graph, start):
        start_x, start_y = start
        graph[start_x][start_y] = 0

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        stack = [start]

        while stack:
            x, y = stack.pop()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m) & (0 <= ny < n):
                    if graph[nx][ny]:
                        stack.append((nx, ny))
                        graph[nx][ny] = 0

        return graph

    for _ in range(t):
        m, n, k = map(int, input().split())
        graph = [[0 for _ in range(n)] for _ in range(m)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[x][y] = 1

        ans = 0
        for x in range(m):
            for y in range(n):
                if graph[x][y]:  # 배추가 심어져있으면 (1이면)
                    ans += 1
                    graph = dfs(graph, (x, y))

        print(ans)


if __name__ == "__main__":
    try1()
