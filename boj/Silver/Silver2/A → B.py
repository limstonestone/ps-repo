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


def try2():
    """
    - 약 15분 소요
    - 가능한 경우의 수가 그렇게 크지 않음 -> 완전탐색
        - 그래프 탐색 알고리즘을 활용하면 각 노드별로 탐색하기 용이
        - 최소값을 구해야하므로 BFS 활용
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    a, b = map(int, input().split())
    visited = dict()

    q = deque([a])
    visited[a] = 1

    while q:
        n = q.popleft()

        n1 = 2 * n
        n2 = int(str(n) + "1")

        for new_n in (n1, n2):
            if new_n <= b and not (new_n in visited):
                visited[new_n] = visited[n] + 1
                q.append(new_n)

    print(visited[b] if b in visited else -1)


if __name__ == "__main__":
    # try1()
    try2()
