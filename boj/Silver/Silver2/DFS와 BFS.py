"""
https://www.acmicpc.net/problem/1260
"""


def try1():
    """
    - 635
    - 방문 가능한 정점이 여러 개 인 경우 정점 번호가 작은 것을 먼저 방문 -> sort
        - 인접 행렬로도 풀이 가능
    - "*" -> 가변 인자로 출력문 처리
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m, v = map(int, input().split())
    graph = []
    for _ in range(n + 1):
        graph.append([])
    for _ in range(m):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
        graph[node1].sort()
        graph[node2].sort()

    def bfs(graph, visited, v, visit_sequence):
        visited = [False] * (n + 1)
        queue = deque([v])
        visited[v] = True

        while queue:
            node = queue.popleft()

            for i in graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visit_sequence.append(i)
                    visited[i] = True

        return visit_sequence

    def dfs(graph, visited, node, visit_sequence):
        visited[node] = True

        for i in graph[node]:
            if not visited[i]:
                visit_sequence.append(i)
                dfs(graph, visited, i, visit_sequence)

    visit_sequence = [v]
    visited = [False] * (n + 1)

    dfs(graph, visited, v, visit_sequence)
    print(*visit_sequence)
    print(*bfs(graph, visited, v, [v]))


if __name__ == "__main__":
    try1()
