"""
https://www.acmicpc.net/problem/15654
"""


def try1():
    """
    - 약 5분 소요
    - 백트래킹으로 풀이
    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    sequence = list(map(int, input().split()))
    sequence.sort()

    seq = []

    def dfs(start):
        if len(seq) == m:
            print(*seq)
            return

        for i in sequence:
            if i not in seq:  # 중복이 일어나지 않도록
                seq.append(i)
                dfs(seq)
                seq.pop()

    dfs(sequence[0])


if __name__ == "__main__":
    try1()
