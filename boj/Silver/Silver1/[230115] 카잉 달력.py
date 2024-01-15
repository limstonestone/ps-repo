"""
https://www.acmicpc.net/problem/6064
"""


def try1():
    """
    - 약 1시간 30분 풀이 후 반례 참조
    - 주어진 대로 반복문으로 구현하면 시간 초과 발생
    - 규칙을 살펴보면 k % m = x, k % n = y 를 만족하는 k 가 답
    - 근데 k 를 어떻게 서치할 것이냐?
        - x 나 y 중 하나를 고정시켜놓고, 배수를 높혀가며 탐색하는 방식
        - 그럼 어디까지 서치할 것? -> 최대 경우의 수 m * n
    - 반례
        - if (k % m == x) & (k % n == y): x==m 또는 y==n 인 경우 성립 X
        - if ((k - x) % m == 0) & ((k - y) % n == 0): 성립 O
    """
    import sys

    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        m, n, x, y = map(int, input().split())

        ans = -1
        k = x

        while k <= m * n:
            # if (k % m == x) & (k % n == y): # x==m 또는 y==n 인 경우 성립 X
            if ((k - x) % m == 0) & ((k - y) % n == 0):
                ans = k
                break
            k += m  # m 의 배수만큼 다시 더해주기, 즉 나머지인 x 는 고정

        print(ans)


if __name__ == "__main__":
    try1()
