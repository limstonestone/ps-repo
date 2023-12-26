"""
https://www.acmicpc.net/problem/1927
"""


def try1():
    """
    - 약 3분 소요
    - n이 최대 10만 -> O(NlogN)
    - heapq 자료구조, 모듈 활용을 묻는 문제
        - heapify 는 사용하지 않아도 문제 없음
        - 시간복잡도 O(log2N)
    """
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())

    heap = []
    # heapq.heapify(heap)

    for _ in range(n):
        x = int(input())
        if x == 0:
            print(0 if not heap else heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)


if __name__ == "__main__":
    try1()
