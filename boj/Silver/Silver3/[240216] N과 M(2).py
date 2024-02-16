"""
https://www.acmicpc.net/problem/15650
"""


def try1():
    """
    - 약 10분 풀이
    - 오름차순의 수열을 생성한 뒤 조합을 이용해서 풀이 가능 (순열은 순서를 고려하므로 X)
    - 백트래킹으로도 풀이 가능
    """
    import sys
    from itertools import combinations as C

    input = sys.stdin.readline

    n, m = map(int, input().split())
    sequence = list(C([x for x in range(1, n + 1)], m))

    for seq in sequence:
        print(*seq)


def try2():
    """
    - 백트래킹 풀이
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    seq = []

    def dfs(start):
        if len(seq) == m:  # 탈출 조건(길이 만족)
            print(*seq)
            return

        for x in range(start, n + 1):
            if x not in seq:  # 수열에 들어있지 않은 숫자 삽입
                seq.append(x)
                dfs(x + 1)
                seq.pop()  # dfs 에서 조건 만족 시 출력 후 제거

    dfs(1)


if __name__ == "__main__":
    try1()
