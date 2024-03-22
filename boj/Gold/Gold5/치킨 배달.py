"""
https://www.acmicpc.net/problem/15686
"""


def try1():
    """
    - 약 35분 소요
    - 그래프 탐색인가? 싶었지만 좌표만 알면 되므로 구현 문제
    - 각 집에서 가장 가까운 치킨집을 어떻게 찾을까?
        - 그냥 최소값으로 직접 구현해도 됨
    - 백트래킹으로도 풀이 가능할듯 함
    """
    import sys
    from itertools import combinations as C

    input = sys.stdin.readline
    n, m = map(int, input().split())
    home, chicken = [], []

    def get_dist(chicken_points):
        dist = 0
        for home_p in home:
            tmp_dist = 1e9
            for chicken_p in chicken_points:
                tmp_dist = min(
                    tmp_dist,
                    abs(home_p[0] - chicken_p[0]) + abs(home_p[1] - chicken_p[1]),
                )  # 여러 치킨집 중 가장 가까운 치킨집과의 거리 찾기
            dist += tmp_dist
        return dist

    for x in range(n):
        line = list(map(int, input().split()))
        for y in range(n):
            if line[y] == 2:
                chicken.append([x, y])
            elif line[y] == 1:
                home.append([x, y])

    dist = 1e9

    # 조합으로 해결한 풀이
    for i in range(1, m + 1):
        for tmp_chicken in C(chicken, i):  # 폐업하지 않을 치킨집 선택
            dist = min(dist, get_dist(tmp_chicken))

    print(dist)

    # 백트래킹으로 해결한 풀이
    arr = []
    visited = [False] * len(chicken)

    def dfs(idx, cnt):
        nonlocal dist
        if cnt == m:
            return

        for i in range(idx, len(chicken)):
            if not visited[i]:
                visited[i] = True
                arr.append(chicken[i])
                dist = min(dist, get_dist(arr))
                dfs(i + 1, cnt + 1)
                arr.pop()
                visited[i] = False

    dist = 1e9
    dfs(0, 0)
    print(dist)


if __name__ == "__main__":
    try1()
