"""
https://www.acmicpc.net/problem/2075
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 힌트 참조
    - 배열에 단순히 저장 후 정렬하여 값을 반환하면 메모리초과 발생
    - 우선 가장 맨 밑에 있는 수 중에 가장 큰 수가 존재함
    - 해당 수부터 위로 올라가다가, 해당 열에 있는 수보다 맨 밑에 있는 다른 수가 더 크다면 해당 수부터 다시 탐색
    - 위 로직을 반복
        - 열에 대한 우선순위를 부여 -> 우선순위 큐? (heap)
        - 위 로직을 어떻게 구현...?

    - 힌트 참조
        - 우선 heap 안에 들어있는 원소의 개수가 N개 미만이라면 heap 안에 원소 입력
        - N개를 채웠다면 현재 숫자가 heap 의 최솟값보다 작은지를 확인
            - 작다면? 어차피 N번째 큰 수의 범위 안에 들 수 없음 (heap 은 N개만을 보관하므로)
            - 크다면? 최솟값을 현재 값으로 대체하여 삽입
        - 예를 들자면, 예제의 1행에서 2행으로 넘어가는 과정에서 heap은 아래와 같음
            - 1행 상태 : [5,7,9,15,12]
            - 2행 상태 : [11,12,13,15,19]
                - 2행의 11, 13, 19가 1행의 5,7,9 보다 크므로 교체
                - 2행의 6이 들어오더라도 8이 더 크므로 교체되고, 들어온 8도 11보다 작으므로 교체됨
    """
    import sys
    import heapq

    input = sys.stdin.readline
    n = int(input())
    heap = []

    for _ in range(n):
        arr = map(int, input().split())
        for x in arr:
            if len(heap) < n:  # heap 의 크기를 n개로 유지
                heapq.heappush(heap, x)
            else:
                if heap[0] < x:
                    heapq.heappop(heap)
                    heapq.heappush(heap, x)

    print(heap[0])


if __name__ == "__main__":
    try1()
