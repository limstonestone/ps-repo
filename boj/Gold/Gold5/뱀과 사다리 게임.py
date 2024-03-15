"""
https://www.acmicpc.net/problem/16928
"""


def try1():
    """
    - 약 30분 소요
    - 그래프 탐색 + 최소 -> BFS
        - 같은 곳을 다시 탐색하면 최소가 될 수 없음
        - 뭔가 그리디가 섞인 것 같기도... (뱀을 안타는게 나으니..? 근데 아닐 수도 있다!)
    - 뱀을 단순히 구현만 해줘도 풀리는 문제였음!
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    graph = [0] * 101

    n, m = map(int, input().split())
    ladders, snakes = dict(), dict()

    for _ in range(n):
        x, y = map(int, input().split())
        ladders[x] = y

    for _ in range(m):
        u, v = map(int, input().split())
        snakes[u] = v

    def bfs(graph):
        q = deque([1])
        graph[1] = 1

        while q:
            node = q.popleft()

            if node == 100:
                return graph[100] - 1

            if node in ladders:  # 현재 노드에 사다리가 있다면
                graph[ladders[node]] = graph[node]  # 방문 + 횟수처리
                node = ladders[node]
            elif node in snakes:  # 현재 노드에 뱀이 있다면
                graph[snakes[node]] = graph[node]  # 방문 + 횟수처리
                node = snakes[node]

            for i in range(1, 7):  # 1부터 6까지 직육면체 굴리기
                new_node = node + i
                if new_node <= 100:
                    if graph[new_node] == 0:  # 방문하지 않은 곳이라면
                        q.append(new_node)
                        graph[new_node] += graph[node] + 1

    print(bfs(graph))


if __name__ == "__main__":
    try1()
