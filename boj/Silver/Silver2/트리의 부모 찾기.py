"""
https://www.acmicpc.net/problem/11725
"""


def try1():
    """
    - 약 35분 풀이
    - 그래프 부모 노드 탐색 -> DFS
    - 첫 방문에 연결되어있는 노드의 부모값을 입력
    """
    import sys

    sys.setrecursionlimit(int(1e9))

    input = sys.stdin.readline

    n = int(input())

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n + 1)

    def dfs(node):
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = node
                dfs(i)

    dfs(1)  # 루트노드에서 탐색 시작

    for i in range(2, n + 1):
        print(visited[i])


def try2():
    """
    - 약 15분 소요
    - DFS 를 활용해 자식노드를 탐색
    - 자식노드를 방문했을 때 이전 부모노드의 값을 딕셔너리에 저장
    """
    import sys

    sys.setrecursionlimit(987654321)

    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    answer = {}
    visited = [False] * (n + 1)

    def dfs(x):
        visited[x] = True

        for i in graph[x]:  # i는 자식노드
            if not visited[i]:
                answer[i] = x  # 부모노드 저장
                dfs(i)

    dfs(1)  # 루트 노드부터 탐색 시작
    for i in range(2, n + 1):
        print(answer[i])


if __name__ == "__main__":
    # try1()
    try2()
