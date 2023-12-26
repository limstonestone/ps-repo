"""
https://www.acmicpc.net/problem/11279
"""


def try1():
    """
    - 약 3분 소요
    - python 의 heapq 모듈과 부호를 활용하여 default 최소힙 -> 최대힙으로 활용 가능
    """
    import sys
    import heapq

    input = sys.stdin.readline

    n = int(input())
    heap = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            print(-heapq.heappop(heap) if heap else 0)

        else:
            heapq.heappush(heap, -x)


if __name__ == "__main__":
    try1()
