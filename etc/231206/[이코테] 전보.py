"""
https://blex.me/@mildsalmon/chap-9-최단-경로-전보
"""


### 1st trial (time : 9:5m)
def try1():
    """
    - 연결된 통로로 최대한 많은 도시로 보내야 함 -> 최단 경로로 보내야 함 -> 최단 경로 문제
    - 노드의 개수인 N 의 범위가 3만이므로 플로이드 워셜 알고리즘은 불가능 -> 다익스트라로 구현
    - INF 처리를 통해 도달할 수 없는 도시 처리가 가능함
    """

    import sys
    import heapq

    input = sys.stdin.readline
    INF = int(1e9)

    N, M, C = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        X, Y, Z = map(int, input().split())
        graph[X].append((Y, Z))

    def dijkstra(start):
        distance = [INF] * (N + 1)
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        return distance

    distance = dijkstra(C)
    cnt, total_time = 0, 0

    for dist in distance:
        if 0 < dist < INF:
            cnt += 1
            total_time = max(total_time, dist)

    print(cnt, total_time)


if __name__ == "__main__":
    try1()
