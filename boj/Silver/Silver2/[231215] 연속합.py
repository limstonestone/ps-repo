"""
https://www.acmicpc.net/problem/1912
"""


def try1():
    """
    - 1시간 고민 후 풀이 실패 -> 힌트 참조
    - n 이 10만 -> O(NlogN) 알고리즘 필요
    - 반복되는 연산을 저장해놓으면 좋음 -> DP
        - 여기서 반복되는 연산 -> 현재 인덱스까지의 총합
        - 누적합을 현재 값부터로 새로 갱신하는 것이 최대냐, 이전 누적합에서 현재값까지의 새로운 누적합이 최대냐
        - 어차피 max(dp) 를 하면 되므로, 지금의 값이 배열 내에서 최대가 아니여도 상관 없음, 새로 갱신할 건지 아닌지의 기준만 되면 됨
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    seq = list(map(int, input().split()))

    dp = [-1000] * n
    dp[0] = seq[0]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + seq[i], seq[i])
        print(dp)

    print(max(dp))


if __name__ == "__main__":
    try1()
