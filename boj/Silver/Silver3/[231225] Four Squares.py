"""
https://www.acmicpc.net/problem/17626
"""


def try1():
    """
    - 약 30분 소요
    - 우선 후보군에 있는 최대한 큰 제곱수를 빼는게 최소의 개수를 보장하기 쉬움
        - 하지만 예시를 들어본 결과 무조건 최대 큰 제곱수를 빼는게 정답이 아닌 것을 알 수 있음
            - 23 의 경우
            - # 23 = 16 + 7 = 16 + (4 + 1  +1 + 1)
            - # 23 = 9 + 9 + 5 = 9 + 9 + (4 + 1)
    - 정답값이 가질 수 있는 최대값은 4
        - n이 최대인 5만이더라도 후보군은 223개
        - 따라서 그냥 가능한 모든 후보군을 직접 대입해보기 -> PyPy 로만 통과
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    dp = [0] * (n + 3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4, n + 1):
        tmp_candidate = [x**2 for x in range(int(i ** (1 / 2)), 0, -1)]
        tmp_candidate = set([dp[i - (candidate)] + 1 for candidate in tmp_candidate])

        dp[i] = min(tmp_candidate)

    print(dp[n])


def solution():
    """
    - 위 풀이는 PyPy 로만 통과
    - DP 풀이는 전부 PyPy 로만 통과 가능한듯 함
    - 브루트포스로도 풀이 가능
    - i ** (1/2) 대신 math.sqrt(i) 가 깔끔하고 직관적인듯 함
    - 해당 풀이는 정답이 최대 4라는 점을 이용하여 경우의 수를 나누어 구현했음
        - 특정 숫자를 뺐을 때 그 수가 제곱수인지 확인하는 작업을 반복
    - 반복문이 많아 보이지만 위 풀이에서 언급했듯이 후보군은 많아봐야 223개이므로 크게 문제없음 (오히려 DP보다 빠름)
    """

    import sys
    import math

    input = sys.stdin.readline

    n = int(input())

    def brute_force(n):
        # 주어진 수 자체가 제곱 수일 때
        if int(math.sqrt(n)) == math.sqrt(n):
            return 1

        # 후보군을 뺐을 때의 수가 제곱 수 (후보군 1개)
        for i in range(1, int(math.sqrt(n)) + 1):
            if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
                return 2

        # 후보군을 뺐을 때의 수가 제곱 수 (후보군 2개)
        for i in range(1, int(math.sqrt(n)) + 1):
            for j in range(1, int(math.sqrt(n - i**2)) + 1):
                if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(
                    n - i**2 - j**2
                ):
                    return 3

        # 이외에는 4개
        return 4

    print(brute_force(n))


if __name__ == "__main__":
    try1()
