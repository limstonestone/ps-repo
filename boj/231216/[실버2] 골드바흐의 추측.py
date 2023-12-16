"""
https://www.acmicpc.net/problem/9020
"""


def try1():
    """
    - 약 8분 소요
    - 짝수를 두 소수의 합으로 나타내기
    - n 이 1만 -> O(NlogN)
    - 두 소수의 차이가 가장 작은 것을 출력해야 함
        - 짝수가 주어지므로, 짝수를 반으로 나눈 숫자부터 출발하여 탐색을 시작한다면 맨 처음 조건을 만족하는 것이 답
    """

    import sys

    input = sys.stdin.readline

    def is_prime_number(x):  # 소수 판별
        for i in range(2, int(x ** (1 / 2)) + 1):
            if x % i == 0:
                return False
        return True

    t = int(input())
    for _ in range(t):
        n = int(input())
        prime_n = n // 2  # 짝수를 반으로 나눠 시작
        while True:
            if is_prime_number(prime_n):
                if is_prime_number(n - prime_n):
                    print(prime_n, n - prime_n)
                    break
            prime_n -= 1


if __name__ == "__main__":
    try1()
