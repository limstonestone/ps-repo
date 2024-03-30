"""
https://www.acmicpc.net/problem/1654
"""


def try1():
    """
    - 약 30분 소요
    - 특정 조건에서 값을 탐색하는데, range 가 sparse 한 문제 -> 이분탐색으로 해결
        - 조건에 맞는 답이 여러 개이지만 그 중 최소/최대를 구해야할 때
    """
    import sys

    input = sys.stdin.readline

    k, n = map(int, input().split())

    lans = [int(input()) for _ in range(k)]
    lans.sort()

    def bin_search(seq, n):
        left, right = 1, 2**31
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            tmp_ans = 0

            for x in seq:
                tmp_ans += x // mid  # 각각 분할 된 랜선 수

            if tmp_ans >= n:
                left = mid + 1
                ans = max(ans, mid)

            elif tmp_ans < n:
                right = mid - 1

        return ans

    print(bin_search(lans, n))


if __name__ == "__main__":
    try1()
