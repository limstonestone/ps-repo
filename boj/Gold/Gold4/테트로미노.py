"""
https://www.acmicpc.net/problem/14500
"""


def try1():
    """
    - 약 55분 소요
    - 그래프 탐색
    - 회전 / 대칭이 있으므로 기준점을 잘 잡아야 함
    - 방문 노드 자체가 필요 없으므로 굳이 BFS/DFS 등의 알고리즘이 필요 없는 구현인 듯함
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    tet1 = [[(1, 0), (1, 0), (1, 0)], [(0, 1), (0, 1), (0, 1)]]
    tet2 = [[(1, 0), (0, -1), (-1, 0)]]
    tet3 = [[(0, -1), (0, -1), (1, 0)], [(-1, 0), (-1, 0), (0, -1)]]
    tet4 = [[(0, -1), (1, 0), (0, -1)], [(-1, 0), (0, -1), (-1, 0)]]
    tet5 = [[(1, 0), (0, -1), (1, 1)], [(0, -1), (-1, 0), (1, -1)]]

    def rotate(tetromino):
        tmp_tetromino = tetromino.copy()
        for tet in tmp_tetromino:
            tetromino.append([(-x, y) for x, y in tet])
            tetromino.append([(x, -y) for x, y in tet])
            tetromino.append([(-x, -y) for x, y in tet])

        return tetromino

    tet1, tet2, tet3, tet4, tet5 = (
        rotate(tet1),
        rotate(tet2),
        rotate(tet3),
        rotate(tet4),
        rotate(tet5),
    )

    def bfs(graph, start):
        ans = 0
        x, y = start[0], start[1]

        for tet in [tet1, tet2, tet3, tet4, tet5]:
            for step in tet:
                tmp_ans = graph[x][y]
                nx, ny = x, y
                for dx, dy in step:
                    nx, ny = nx + dx, ny + dy
                    if (0 <= nx < n) and (0 <= ny < m):
                        tmp_ans += graph[nx][ny]

                ans = max(ans, tmp_ans)

        return ans

    ans = 0
    for x in range(n):
        for y in range(m):
            ans = max(ans, bfs(graph, (x, y)))

    print(ans)


if __name__ == "__main__":
    try1()
