"""
https://www.acmicpc.net/problem/2292
"""


def try1():
    """
    - 약 30분 소요
    - 입력 범위가 10억으로 매우 큼 -> 배열에 담는 것은 최대한 자제
    - 규칙(점화식)이 존재할 것이라 판단하여 관찰
        - 1 = 1
        - 2~7 = 2 (6개 존재)
        - 8~19 = 3 (12개 존재)
        - 번호의 수는 6 * i 로 나타낼 수 있음 (i = 건너가는 방의 수)
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    i, ans = 1, 1

    while i < n:
        i = (i) + 6 * ans
        ans += 1

    print(ans)


if __name__ == "__main__":
    try1()
