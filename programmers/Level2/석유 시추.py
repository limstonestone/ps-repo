"""
https://school.programmers.co.kr/learn/courses/30/lessons/250136
"""


def solution(land):
    """
    - 약 1시간 소요
    - BFS/DFS로 하나의 연결된 지점마다 석유의 총 내장량을 찾고 이를 Return
        - 중복을 최소화하지않으면 시간초과 발생
        - 즉 모든 row, col 을 순회하는 이중 반복문 -> 시간초과
    - 집합을 활용하여 한번 탐색할 때 해당 좌표가 뻗어있는 석유의 y 좌표를 반환하여 중복 최소화
    - 최종적으로 oil_by_col 딕셔너리에 각 컬럼별 시추량을 저장
        - 예제2 예시) {1:12, 2:12, 3:15, 4:14, 5:14, 6:16}
    """

    from collections import deque, defaultdict

    m, n = len(land), len(land[0])
    oil_loc = []

    # 석유가 존재하는 좌표 찾기
    for y in range(n):
        for x in range(m):
            if land[x][y] == 1:
                oil_loc.append([x, y])

    def bfs(graph, start):
        q = deque([start])
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 1
        visited[start[0]][start[1]] = True
        y_oiled = set([start[1]])  # 오일이 존재하는 y좌표를 반환하는 집합

        while q:
            x, y = q.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (
                    (0 <= nx < m)
                    and (0 <= ny < n)
                    and (graph[nx][ny] == 1)
                    and (not visited[nx][ny])
                ):
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
                    if ny not in y_oiled:
                        y_oiled.add(ny)  # 새로 방문한 곳(오일이 존재하는)의 y좌표 저장

        return cnt, y_oiled

    visited = [[False for _ in range(n)] for _ in range(m)]
    oil_by_col = defaultdict(int)  # 컬럼별로 석유 시추량이 저장되어있는 dictionary

    for row, col in oil_loc:  # 오일이 존재하는 좌표들 탐색
        if not visited[row][col]:  # BFS 를 통해 방문된 좌표는 pass
            oil, y_loc = bfs(
                land, [row, col]
            )  # 해당 좌표의 시추량, 그리고 해당 좌표의 석유가 뻗어있는 y 좌표 반환
            for y in y_loc:  # 여러 y좌표들이 존재하므로 각각 시추량 담아줌
                oil_by_col[y] += oil

    answer = max(oil_by_col.values())
    return answer
