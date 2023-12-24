"""
https://www.acmicpc.net/problem/1764
"""


def try1():
    """
    - 약 2분 소요
    - 집합 메소드를 활용하는 문제
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())

    no_listend, no_seen = set(), set()

    for _ in range(n):
        no_listend.add(input().rstrip())

    for _ in range(m):
        no_seen.add(input().rstrip())

    no_both = list(no_listend.intersection(no_seen))

    no_both.sort()
    print(len(no_both))
    for x in no_both:
        print(x)


if __name__ == "__main__":
    try1()
