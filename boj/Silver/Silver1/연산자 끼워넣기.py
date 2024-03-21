"""
https://www.acmicpc.net/problem/14888
"""


def try1():
    """
    - 약 1시간 소요
    - 백트래킹을 활용할 수 있지만, 연산자의 최대 길이가 10이므로 순열로 구현해도 문제없을 듯 함
    - 파이썬의 문자열 연산 내장함수 -> eval() 활용
    """
    import sys
    from itertools import permutations as P

    input = sys.stdin.readline

    n = int(input())
    A = input().split()
    plus, minus, mul, div = map(int, input().split())
    operators = ["+"] * plus + ["-"] * minus + ["*"] * mul + ["/"] * div
    total_operators = list(
        set(P(operators, n - 1))
    )  # set -> 연산자의 순서를 고려하지만 중복된 연산자의 경우 제거
    max_ans, min_ans = -1000000000, 1000000000  # 10억 초기화

    for operators in total_operators:
        answer = A[0]
        for i, op in enumerate(operators):
            answer = int(eval(str(answer) + op + A[i + 1]))

        max_ans, min_ans = max(max_ans, answer), min(min_ans, answer)

    print(max_ans)
    print(min_ans)


if __name__ == "__main__":
    try1()
