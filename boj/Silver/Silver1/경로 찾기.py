"""
https://www.acmicpc.net/problem/11403
"""


def try1():
    """
    - 약 30분 소요
    - 그래프 탐색 문제
        - 방향이 있다는 점만 주의해서 풀이
    - 최단경로가 양수이냐 아니냐이므로 플로이드 워셜로도 풀이 가능
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = [[0] * n for _ in range(n)]

    def dfs(graph, visited, i, target):
        stack = [i]

        while stack:
            node = stack.pop()
            for c in range(len(graph[node])):
                if (graph[node][c] == 1) & (not visited[c]):
                    visited[c] = True
                    if c == target:
                        return 1
                    stack.append(c)
        return 0

    ### 아래 부분 필요 없이 행마다 직접 answer 를 생성해내도 됨
    for x in range(n):
        for y in range(n):
            visited = [False] * n
            ans = dfs(graph, visited, x, y)
            answer[x][y] = ans

    ### 즉, 아래 부분에서 dfs 를 수행해서 행마다 출력할 수도 있음
    for i in range(n):
        print(*answer[i])


if __name__ == "__main__":
    try1()
