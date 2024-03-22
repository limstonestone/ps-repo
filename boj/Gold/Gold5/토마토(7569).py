"""
https://www.acmicpc.net/problem/7569
"""


def try1():
    """
    - 약 23분 소요
    - 그래프 탐색 + 최단거리 -> BFS
        - 이때, 그래프가 3차원임을 유의
        - 따라서 원하는 좌표를 찾으려면 z, y, x (x,y,z 역순) 순으로 인덱싱
    - 데이터 정의만 잘 해준다면 2차원 BFS 와 다를 것 없음
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    m, n, h = map(int, input().split())

    graph = [[] for _ in range(h)]
    tomato = []

    for z in range(h - 1, -1, -1):
        for y in range(n):
            tmp = list(map(int, input().split()))
            ls = []
            for x in range(m):
                ls.append(tmp[x])
                if tmp[x] == 1:
                    tomato.append((z, y, x))
            graph[z].append(ls)

    def bfs(graph, tomato):
        q = deque(tomato)
        direction = [
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        ]

        while q:
            z, y, x = q.popleft()

            for dx, dy, dz in direction:
                nx, ny, nz = x + dx, y + dy, z + dz

                if (0 <= nx < m) & (0 <= ny < n) & (0 <= nz < h):
                    if graph[nz][ny][nx] == 0:
                        graph[nz][ny][nx] += graph[z][y][x] + 1
                        q.append((nz, ny, nx))

        return graph

    graph = bfs(graph, tomato)
    ans = 0

    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:  # 익지 못한 토마토가 존재한다면 바로 실패
                    print(-1)
                    exit()
                elif graph[z][y][x] != -1:
                    ans = max(ans, graph[z][y][x])

    print(ans - 1)


def try2():
    """
    - 약 45분 소요
    - 최소 횟수 그래프탐색 -> BFS
    - Z축이 새로 생긴 그래프탐색 문제와 같음
    - 토마토 좌표를 한꺼번에 입력하여 해결
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    m, n, h = map(int, input().split())

    graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

    def bfs(graph, start):
        q = deque(start)
        direction = [
            [0, 1, 0],
            [1, 0, 0],
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, 1],
            [0, 0, -1],
        ]

        while q:
            x, y, z = q.popleft()

            for dx, dy, dz in direction:
                nx, ny, nz = x + dx, y + dy, z + dz
                if (
                    (0 <= nx < n)
                    and (0 <= ny < m)
                    and (0 <= nz < h)
                    and (graph[nz][nx][ny] == 0)
                ):
                    q.append([nx, ny, nz])
                    graph[nz][nx][ny] = graph[z][x][y] + 1

        ans = 0
        for x in range(n):
            for y in range(m):
                for z in range(h):
                    if graph[z][x][y] == 0:  # 익지못한 토마토가 존재하면 바로 -1 리턴
                        return -1
                    ans = max(graph[z][x][y], ans)

        return ans - 1

    tomato = []
    for x in range(n):
        for y in range(m):
            for z in range(h):
                if graph[z][x][y] == 1:
                    tomato.append([x, y, z])

    result = bfs(graph, tomato)
    print(result)


if __name__ == "__main__":
    # try1()
    try2()
