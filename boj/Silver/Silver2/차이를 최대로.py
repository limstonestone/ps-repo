"""
- https://www.acmicpc.net/problem/10819
"""


def try1():
    """
    - 약 3분 소요
    - 입력 길이 최대8로 매우 짧음 -> 순열로 직접 구현
    - 백트래킹으로도 풀이 가능
    """
    import sys
    from itertools import permutations as P

    input = sys.stdin.readline

    n = int(input())
    seq = list(map(int, input().split()))
    ans = 0

    # 순열 풀이
    for arr in P(seq):
        tmp_ans = 0
        for i in range(n - 1):
            tmp_ans += abs(arr[i] - arr[i + 1])
        ans = max(ans, tmp_ans)

    print(ans)

    # 백트래킹 풀이
    visited = [False] * n

    def dfs(tmp_arr):
        nonlocal ans

        if len(tmp_arr) == n:
            tmp_ans = 0
            for i in range(n - 1):
                tmp_ans += abs(tmp_arr[i] - tmp_arr[i + 1])
            ans = max(ans, tmp_ans)
            return

        for i in range(n):
            if not visited[i]:
                tmp_arr.append(seq[i])
                visited[i] = True
                dfs(tmp_arr)
                visited[i] = False
                tmp_arr.pop()

    dfs([])
    print(ans)


if __name__ == "__main__":
    try1()
