"""
https://blex.me/@mildsalmon/chap-9-최단-경로-미래-도시
"""


### 1st trial (time : 40m)
def try1():
    """
    - 특정 지점에서 특정 지점까지의 최단 경로 -> 다익스트라
    - 다익스트라를 숙지하고 양방향인점만 주의하면 무리없이 풀 수 있는듯 함
    """

    import sys
    import heapq

    input = sys.stdin.readline

    INF = int(1e9)

    N, M = map(int, input().split())
    graph = [[] for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append((1, b))
        graph[b].append((1, a))

    X, K = map(int, input().split())

    def dijkstra(start, end):
        distance = [INF] * (N + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[0]

            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

        return distance[end]

    A2K = dijkstra(1, K)
    K2X = dijkstra(K, X)

    ans = A2K + K2X

    if ans >= INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    try1()
