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


def try2():
    """
    - 약 50분 풀이
    - 기준점을 잡아 테트로미노의 회전과 대칭을 고려해야함이 핵심
    - 그래프탐색 알고리즘을 사용할 필요는 없음
    - 회전과 대칭을 고려하기가 조금 복잡할 수 있지만, 회전4 * 대칭2 = 8
        - 이를 고려해보면 아래 transform 함수를 쉽게 도출 가능
    """

    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]

    tet1 = [(1, 0), (1, 0), (1, 0)]  # ㅡ 모양
    tet2 = [(1, 0), (0, -1), (-1, 0)]  # ㅁ 모양
    tet3 = [(0, -1), (0, -1), (1, 0)]  # L 모양
    tet4 = [(1, 0), (0, -1), (1, 1)]  # ㅜ 모양
    tet5 = [(0, -1), (1, 0), (0, -1)]  # 남은 모양

    def transform(tet_lst):  # 90도 회전 4번 * 각각 대칭
        transformed_tet = []
        for tet in tet_lst:
            tmp_tet = []
            tmp_tet.append([(x, y) for x, y in tet])
            tmp_tet.append([(-x, y) for x, y in tet])
            tmp_tet.append([(x, -y) for x, y in tet])
            tmp_tet.append([(-x, -y) for x, y in tet])
            tmp_tet.append([(y, x) for x, y in tet])
            tmp_tet.append([(-y, x) for x, y in tet])
            tmp_tet.append([(y, -x) for x, y in tet])
            tmp_tet.append([(-y, -x) for x, y in tet])
            transformed_tet.append(tmp_tet)

        return transformed_tet

    tet1, tet2, tet3, tet4, tet5 = transform([tet1, tet2, tet3, tet4, tet5])

    def search(x, y):
        ans = 0
        for total_tet in (tet1, tet2, tet3, tet4, tet5):  # 8개의 변환된 테트로미노 추출
            for tet in total_tet:  # 각 테트로미노 확인
                tmp_ans = graph[x][y]  # 현재 좌표값도 포함
                nx, ny = x, y
                for dx, dy in tet:
                    nx += dx
                    ny += dy
                    if 0 <= nx < n and 0 <= ny < m:
                        tmp_ans += graph[nx][ny]
                    else:  # 중간에 테트로미노가 범위를 벗어난다면 실패 처리
                        tmp_ans = 0
                        break
                ans = max(ans, tmp_ans)

        return ans

    ans = 0
    for x in range(n):
        for y in range(m):
            ans = max(ans, search(x, y))

    print(ans)


if __name__ == "__main__":
    # try1()
    try2()
