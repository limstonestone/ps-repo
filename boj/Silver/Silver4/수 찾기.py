"""
https://www.acmicpc.net/problem/1920
"""


def try1():
    """
    - 약 2분 소요
    - set 자료형을 활용하면 in 연산이 O(1)로 가능
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    A = set(list(map(int, input().split())))

    m = int(input())
    seq_m = list(map(int, input().split()))

    for i in range(m):
        print(1 if seq_m[i] in A else 0)


def try2():
    """
    - 약 12분 소요
    - 특정 값에 대한 탐색 -> 정렬 후 이분탐색
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    A = list(map(int, input().split()))

    m = int(input())
    numbers = list(map(int, input().split()))

    A.sort()

    def bin_search(seq, num):
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if seq[mid] < num:
                left = mid + 1
            elif seq[mid] > num:
                right = mid - 1
            else:  # 정확하게 찾았을 때
                return mid

        return -1

    for num in numbers:
        idx = bin_search(A, num)
        print(1 if idx != -1 else 0)


if __name__ == "__main__":
    # try1()
    try2()
