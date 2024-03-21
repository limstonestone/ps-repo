"""
https://www.acmicpc.net/problem/14502
"""


def try1():
    """
    - 약 26분 소요
    - 그래프 탐색 -> BFS
    - 가로, 세로 길이가 3~8 사이이므로 매우 작음 -> 러프하게 구현하되, 시간복잡도를 줄일 수 있는 부분에서는 줄이기
    - 그래프를 입력 받을 때 바이러스와 후보군 좌표(값이 0)을 미리 입력받음
        - 이후 BFS 시 해당좌표들만 활용

    - 이후 찾아보니 벽을 구축하는 과정에서 백트래킹을 활용하는 방식이 있는데 훨씬 직관적인듯함
        - 이번 문제에서는 입력 길이가 작기 때문에 조합을 구하는 과정에서 메모리가 적게 들어 현재 풀이가 시간이 덜 소요되긴 함
    """
    import sys
    from collections import deque, Counter
    from itertools import combinations as C
    from copy import deepcopy

    input = sys.stdin.readline

    n, m = map(int, input().split())

    maps = []
    candidate_loc, virus_loc = [], []

    for x in range(n):
        line = list(map(int, input().split()))
        maps.append(line)

        for y in range(m):
            if line[y] == 0:
                candidate_loc.append([x, y])  # 벽을 둘 후보군 좌표 집합
            elif line[y] == 2:
                virus_loc.append([x, y])  # 바이러스 좌표 집합

    ans = 0

    def bfs(graph, virus, candidates):
        graph = deepcopy(graph)  # 원본이 훼손되지 않도록 deepcopy

        for x, y in candidates:
            graph[x][y] = 1

        q = deque(virus)
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = 2  # 벽이 없다면 바이러스 침투

        return graph

    total_candidates = C(candidate_loc, 3)  # 가능한 3개의 모든 좌표 계산

    for candidates in total_candidates:
        tmp_ans = 0
        result = bfs(maps, virus_loc, candidates)

        for row in result:
            tmp_ans += Counter(row)[0]  # Counter 활용하여 0의 개수 계산

        ans = max(tmp_ans, ans)

    print(ans)


if __name__ == "__main__":
    try1()
