"""
https://www.acmicpc.net/problem/16953
"""


def try1():
    """
    - 약 15분 소요
    - DP? BFS? -> 입력의 범위가 매우 넓으므로 DP 테이블을 만드는 것은 불가능할듯 함
    - 방문을 계속하다가 조건에 맞았을 시 최소값 리턴 -> BFS
    - BFS 도 visited 배열을 딕셔너리로 활용하여 큰 scale 문제로 인한 공간복잡도를 줄일 수 있음
    """
    import sys
    from collections import deque

    input = sys.stdin.readline
    a, b = map(int, input().split())

    visited = dict()
    q = deque([a])
    visited[a] = 1

    while q:
        node = q.popleft()
        if node == b:
            break

        for i in [node * 2, int(str(node) + "1")]:
            if (i <= b) and (i not in visited):
                q.append(i)
                visited[i] = visited[node] + 1

    print(visited[b] if b in visited else -1)


if __name__ == "__main__":
    try1()
