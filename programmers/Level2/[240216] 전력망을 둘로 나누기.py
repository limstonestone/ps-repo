"""
https://school.programmers.co.kr/learn/courses/30/lessons/86971
"""


def solution(n, wires):
    """
    - 약 20분 풀이
    - 인접한 그래프 탐색 -> BFS/DFS
    - 이 때 강제로 연결관계를 절단시킴
        - 어디를 절단시켜야 최소차이를 보일지 패턴을 잡기에는 어려워보임
        - 엣지가 100 이하이므로 완전탐색으로 구현해보자

    - 타인 풀이
        - 굳이 그래프 절단을 매번 동기화하지 않고, visited 부분을 True 처리해주면 절단된것과 마찬가지
    """
    from collections import deque

    answer = 1e9

    def bfs(graph, start, cut):
        q = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        visited[cut[0]], visited[cut[1]] = True, True
        cnt = 0

        while q:
            node = q.popleft()
            for new_node in graph[node]:
                if not visited[new_node]:
                    visited[new_node] = True
                    cnt += 1
                    q.append(new_node)

        return cnt

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n - 1):
        left, right = bfs(graph, wires[i][0], wires[i]), bfs(
            graph, wires[i][1], wires[i]
        )
        answer = min(answer, abs(left - right))

    return answer
