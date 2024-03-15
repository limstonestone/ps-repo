"""
https://www.acmicpc.net/problem/11724
"""


def try1():
    """
    - 약 20분 소요
    - 그래프 탐색 문제 -> DFS/BFS
    - 방문한 노드에 연결되어있는 간선 값들을 전부 0으로 만들어 연결 요소의 개수를 구할 수 있음
    """
    import sys

    sys.setrecursionlimit(int(1e9))

    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # 1부터 시작하므로 n+1
    visited = [False] * (n + 1)

    for _ in range(m):
        node1, node2 = map(int, input().split())
        graph[node1][node2] = 1
        graph[node2][node1] = 1

    def dfs(graph, v, visited):
        visited[v] = True
        for i in range(1, n + 1):
            if graph[v][i] == 1 and not visited[i]:
                graph[v][i] = 0
                dfs(graph, i, visited)

    ans = 0

    for i in range(1, n + 1):
        if not visited[i]:
            ans += 1
            dfs(graph, i, visited)

    print(ans)


if __name__ == "__main__":
    try1()
