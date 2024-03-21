"""
https://www.acmicpc.net/problem/14889
"""


def try1():
    """
    - 약 15분 소요
    - 재귀 활용 백트래킹? -> 입력 길이가 최대 20이므로 combination 으로 모든 경우의 수를 구현하더라도 최대 10C2
    - 입력 길이 최대일 때 경우의 수 -> 20C10 이므로 조합으로 구현해서 풀이 가능할듯 함
    """
    import sys
    from itertools import combinations as C

    input = sys.stdin.readline

    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]

    total_start = C(range(n), n // 2)
    ans = 1e9

    for start in total_start:
        link = sorted(set(range(n)) - set(start))
        start_ans, link_ans = 0, 0

        for (start_a, start_b), (link_a, link_b) in zip(C(start, 2), C(link, 2)):
            start_ans += S[start_a][start_b] + S[start_b][start_a]
            link_ans += S[link_a][link_b] + S[link_b][link_a]

        ans = min(abs(start_ans - link_ans), ans)

    print(ans)


if __name__ == "__main__":
    try1()
