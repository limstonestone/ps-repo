"""
https://www.acmicpc.net/problem/2606
"""


def try1():
    """
    - 약 18분 소요
    - 네트워크의 구조가 그래프 탐색 문제와 같음 -> DFS/BFS
        - 양방향 구조 & self loop 존재 X
    - nonlocal 명령어 사용 시 함수안의 함수의 지역변수를 전역변수로 설정 가능
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    e = int(input())  # edge

    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    visited = [False for _ in range(n + 1)]

    ans = 0

    def dfs(graph, visited, v):
        nonlocal ans
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                ans += 1
                dfs(graph, visited, i)

    dfs(graph, visited, 1)

    print(ans)


if __name__ == "__main__":
    try1()
