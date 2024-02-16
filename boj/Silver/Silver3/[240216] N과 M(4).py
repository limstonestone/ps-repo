"""
https://www.acmicpc.net/problem/15652
"""


def try1():
    """
    - 약 3분 소요
    - 백트래킹으로 풀이 가능
    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    seq = []

    def dfs(start):
        if len(seq) == m:
            print(*seq)
            return

        for x in range(start, n + 1):
            seq.append(x)
            dfs(x)  # 길이를 만족할 때 까지 수열 삽입
            seq.pop()  # 길이를 만족했다면 출력하고 증가하는 숫자가 앞으로 들어올 것

    dfs(1)


if __name__ == "__main__":
    try1()
