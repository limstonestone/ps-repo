"""
https://www.acmicpc.net/problem/15683
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 힌트 참조 + 1시간 풀이
    - 벽을 통과하지 않는 한 뚫려있는 0들은 전부 #으로 가능
    - CCTV 개수가 최대 8개이므로 완전탐색
        - 백트래킹으로 원래 상태를 다시 복원하는 과정 구현 가능

    - 답지 참조
        - 회전 방향을 잘 못 잡았었음, 일일히 다시 구현
    """
    import sys
    from copy import deepcopy

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = []
    cctv = []
    answer = 0

    for x in range(n):
        arr = list(map(int, input().split()))
        graph.append(arr)
        answer += arr.count(0)
        for y in range(m):
            if 1 <= arr[y] <= 5:
                cctv.append([arr[y], x, y])

    k = len(cctv)

    direction = {
        1: [[(1, 0)], [(0, 1)], [(0, -1)], [(-1, 0)]],
        2: [[(1, 0), (-1, 0)], [(0, -1), (0, 1)]],
        3: [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)], [(-1, 0), (0, 1)]],
        4: [
            [(0, 1), (-1, 0), (1, 0)],
            [(0, 1), (1, 0), (0, -1)],
            [(-1, 0), (0, -1), (1, 0)],
            [(0, -1), (-1, 0), (0, 1)],
        ],
        5: [[(1, 0), (0, 1), (-1, 0), (0, -1)]],
    }

    def move(x, y, dir, tmp_graph):
        for dx, dy in dir:
            nx, ny = x, y

            while True:
                nx += dx
                ny += dy
                if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] != 6:
                    if tmp_graph[nx][ny] == 0:
                        tmp_graph[nx][ny] = "#"
                else:
                    break

    def dfs(graph, cnt):
        nonlocal answer
        if cnt == k:
            answer = min(answer, sum(graph[x].count(0) for x in range(n)))
            return

        type_, x, y = cctv[cnt]

        for dir in direction[type_]:
            tmp_graph = deepcopy(graph)
            move(x, y, dir, tmp_graph)  # 현재 CCTV 처리하기
            dfs(tmp_graph, cnt + 1)  # 다음 CCTV 탐색

    dfs(graph, 0)
    print(answer)


if __name__ == "__main__":
    try1()
