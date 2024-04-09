"""
https://www.acmicpc.net/problem/2644
"""


def try1():
    """
    - 약 10분 소요
    - DFS 문제
    """
    import sys
    from collections import defaultdict

    input = sys.stdin.readline
    n = int(input())
    n1, n2 = map(int, input().split())
    m = int(input())

    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (n + 1)
    ans = -1

    def dfs(node, cnt):
        nonlocal ans
        visited[node] = True

        if node == n2:
            ans = cnt
            return

        for new_node in graph[node]:
            if not visited[new_node]:
                dfs(new_node, cnt + 1)

    dfs(n1, 0)
    print(ans)


if __name__ == "__main__":
    try1()
