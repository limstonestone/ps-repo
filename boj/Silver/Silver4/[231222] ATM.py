"""
https://www.acmicpc.net/problem/11399
"""


def try1():
    """
    - 약 10분 소요
    - 입력 n 의 범위는 1000 -> O(N^3) 까지 가능
    - 짧게 인출이 가능한 사람이 앞에 올수록 총 대기시간이 짧아짐 -> 그리디
        - 모든 순열을 구할 필요가 없음 (브루트 포스 X)
    - 각 원소가 더해지는 횟수는 1~n 이므로 누적합으로 구현하기보다는 곱셈으로 구현
    """
    import sys

    input = sys.stdin.readline
    n = int(input())

    P = list(map(int, input().split()))

    P.sort(reverse=True)
    ans = 0

    for i in range(n):
        ans += (i + 1) * P[i]

    print(ans)


if __name__ == "__main__":
    try1()
