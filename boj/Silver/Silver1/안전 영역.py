"""
https://www.acmicpc.net/problem/2468
"""


def try1():
    """
    - 약 40분 소요
    - 그래프 탐색 문제
    - 입력 크기가 작으므로 반복문 활용해서 러프하게 구현해도 될 듯함
    - 주의) 모두 1로 채워져있는 경우 return 값이 0이 아닌 1이여야함 (전부 다 잠기는 건데 왜 ..?)
    """
    import sys
    from collections import deque
    from copy import deepcopy

    input = sys.stdin.readline

    n = int(input())

    origin_graph = [list(map(int, input().split())) for _ in range(n)]

    def bfs(graph, start):
        q = deque([start])
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited[start[0]][start[1]] = True

        while q:
            x, y = q.popleft()
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (
                    (0 <= nx < n)
                    and (0 <= ny < n)
                    and (not visited[nx][ny])
                    and (graph[x][y] != -1)
                ):
                    q.append([nx, ny])
                    visited[nx][ny] = True

        return 1

    ans = 1  # 위에서 언급한 반례를 위해 0이 아닌 1로 초기화
    for h in range(1, 100 + 1):
        tmp_ans = 0
        candidates = []
        visited = [[False for _ in range(n)] for _ in range(n)]
        graph = deepcopy(origin_graph)
        for x in range(n):
            for y in range(n):
                if graph[x][y] <= h:
                    graph[x][y] = -1  # 잠긴 상황 구현
                else:
                    candidates.append([x, y])  # 잠기지 않은 좌표를 통해 BFS탐색

        if (
            not candidates
        ):  # candidates 가 없으면, 즉 모두 비에 잠겼으면 탐색할 필요 없음
            break

        for x, y in candidates:
            if not visited[x][y]:
                tmp_ans += bfs(graph, [x, y])  # BFS를 통해 방문처리 후 영역 하나 반환

        ans = max(ans, tmp_ans)

    print(ans)


if __name__ == "__main__":
    try1()
