"""
https://www.acmicpc.net/problem/15666
"""


def try1():
    """
    - 약 10분 풀이
    - 백트래킹, N과 M(9)와 매우 유사
    - 중복이 허용되므로 이전 수와 현재 수가 같은지, 아닌지만 판별하면 됨
        - ex) 7 9 9
            - 7 9, 7 9 가 되지 않도록 (첫번째 9 == 두번째 9)
    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    seq = []

    def dfs(start):
        if len(seq) == m:
            print(*seq)
            return

        for i in range(start, n):  # 이전에 사용한 루트는 사용하지않으므로 start 부여
            if (i > 0) and (
                nums[i] == nums[i - 1]
            ):  # 이전 수와 현재 수가 같다면 사용 X (이전에 출력이 이미 되었으니), 첫번째 수는 무조건 사용
                continue

            seq.append(nums[i])
            dfs(i)
            seq.pop()

    dfs(0)


if __name__ == "__main__":
    try1()
