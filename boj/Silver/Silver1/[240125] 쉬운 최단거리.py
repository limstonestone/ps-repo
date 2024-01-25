"""
https://www.acmicpc.net/problem/14940
"""


def try1():
    """
    - 약 1시간 소요
    - 특정 지점에서 모든 지점에 대한 최단거리(방문) -> BFS
    - 다익스트라로도 풀이 가능할듯 함 (BFS가 더 빠름)
    - 반례 하나 때문에 굉장히 오랜 시간 소요
        - <예시>
        - 2 2
        - 2 0
        - 0 0
        - 위 경우 대각선의 0이 -1로 찍히는 문제 발생
        - visited 의 default 값을 graph 가 1일땐 -1, 아닐땐 0으로 해야 해결가능
            - 원래 그래프가 0인 경우 큐에 삽입하지 않으므로
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    target = None

    for x in range(n):
        tmp_map = list(map(int, input().split()))
        graph.append(tmp_map)

        if not target:
            for y in range(m):
                if tmp_map[y] == 2:
                    target = (x, y)

    def bfs(start):
        visited = []
        for x in range(n):
            tmp_list = []
            for y in range(m):
                tmp_list.append(-1 if graph[x][y] != 0 else 0)
            visited.append(tmp_list)

        q = deque([start])
        x, y = start
        visited[x][y] = 0
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n) & (0 <= ny < m):
                    if visited[nx][ny] == -1:
                        if graph[nx][ny] == 1:
                            q.append((nx, ny))
                            visited[nx][ny] = visited[x][y] + 1

        return visited

    distance = bfs(target)
    for dist in distance:
        print(*dist)


if __name__ == "__main__":
    try1()
