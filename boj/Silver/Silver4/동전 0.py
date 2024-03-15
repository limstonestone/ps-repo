"""
https://www.acmicpc.net/problem/11047
"""


def try1():
    """
    - 약 10분 소요
    - 최소의 횟수가 되려면 가장 큰 수를 먼저 뺄수있는만큼 최대한 빼야함 -> 그리디
        - 몫과 나머지를 활용하여 시간복잡도 줄일 수 있음
    """
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    coin_value = []
    for _ in range(n):
        value = int(input().rstrip())
        if value > k:
            continue
        coin_value.append(value)

    ans = 0
    while k != 0:
        max_value = coin_value.pop()
        mok, k = divmod(k, max_value)
        ans += mok

    print(ans)


if __name__ == "__main__":
    try1()
