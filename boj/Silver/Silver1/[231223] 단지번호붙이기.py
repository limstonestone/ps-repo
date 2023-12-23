"""
https://www.acmicpc.net/problem/2667
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 한 단지를 찾고나면 BFS 가 종료되므로, 모든 점에 대해서 탐색 시작
        - 이 때 시작점이 1인 경우만 단지가 존재함
        - 방문 배열없이 직접 그래프의 값을 0으로 변경 (더 이상 단지 탐색을 할 필요가 없음)
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())

    graph = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = []

    def bfs(graph, start):
        queue = deque([start])
        graph[start[0]][start[1]] = 0
        cnt = 1

        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            x, y = queue.popleft()

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if (0 <= nx < n) & (0 <= ny < n):
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        queue.append((nx, ny))
                        cnt += 1

        return graph, cnt

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                graph, cnt = bfs(graph, (i, j))
                ans.append(cnt)

    ans.sort()

    print(len(ans))
    for x in ans:
        print(x)


if __name__ == "__main__":
    try1()
