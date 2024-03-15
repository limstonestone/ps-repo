"""
https://www.acmicpc.net/problem/11286
"""


def try1():
    """
    - 약 30분 소요
    - 튜플(절댓값, 부호) 형태로 heap 에 입력하면 절댓값이 작은 순서대로 pop
    - 이 떄, 같은 값이 있다면 두 번째 부호가 작은(최소 힙) 값을 출력한다는 아이디어를 활용
    """
    import sys
    import heapq

    input = sys.stdin.readline
    n = int(input())

    heap = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            if heap:
                val, sign = heapq.heappop(heap)
                print(sign * val)
            else:
                print(0)
        else:
            heapq.heappush(heap, (abs(x), 1 if x > 0 else -1))


if __name__ == "__main__":
    try1()
