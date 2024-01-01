"""
https://www.acmicpc.net/problem/1389
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 그래프 탐색 & 최단 거리 -> BFS

    - 답지 풀이
        - 큐에 입력할 때 step 이라는 값을 노드와 함께 튜플 형태로 입력하여 각 노드마다 다른 정답 값을 보유하도록 함
        - 또한 종점을 정해놓을 필요 없이, 단순히 모든 노드에 대한 탐색이 끝나면 다 더해주면 됨
    """

    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(user):
        visited = [False] * (n + 1)
        ans = [0] * (n + 1)
        queue = deque([(user, 0)])
        visited[user] = True

        while queue:
            cur_user, steps = queue.popleft()
            ans[cur_user] = steps

            for friend in graph[cur_user]:
                if not visited[friend]:
                    visited[friend] = True
                    queue.append((friend, steps + 1))

        return sum(ans[1:])

    min_ans = float("inf")
    min_user = -1

    for user in range(1, n + 1):
        cur_ans = bfs(user)
        if cur_ans < min_ans:
            min_ans = cur_ans
            min_user = user

    print(min_user)


if __name__ == "__main__":
    try1()
