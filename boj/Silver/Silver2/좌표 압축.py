"""
https://www.acmicpc.net/problem/18870
"""


def try1():
    """
    - 약 10분 소요
    - n이 100만 -> O(N)
    - 딕셔너리(key-value)를 활용하여 시간복잡도를 단축하여 해결
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().split()))

    num_set = sorted(set(numbers))
    num_set = dict(zip(num_set, range(len(num_set))))

    new_numbers = [num_set[x] for x in numbers]
    print(*new_numbers)


if __name__ == "__main__":
    try1()
