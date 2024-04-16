"""
https://www.acmicpc.net/problem/13549
"""


def try1():
    """
    - 약 15분 소요
    - 약간의 조건이 추가된 최단거리 탐색 -> BFS
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, k = map(int, input().split())
    visited = [1e9] * (100_000 + 1)

    q = deque([n])
    visited[n] = 0

    while q:
        now = q.popleft()

        for i, new_loc in enumerate([now - 1, now + 1, 2 * now]):
            # 범위 안에 들어오면서 새로운 이동이 기존 값보다 더 단축시킬 수 있는 경우
            if 0 <= new_loc <= 100_000 and visited[new_loc] > visited[now]:
                visited[new_loc] = visited[now] + 1 if i != 2 else visited[now]
                q.append(new_loc)

    print(visited[k])


if __name__ == "__main__":
    try1()
