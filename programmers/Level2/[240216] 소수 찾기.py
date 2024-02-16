"""
https://school.programmers.co.kr/learn/courses/30/lessons/42839
"""


def solution(numbers):
    """
    - 약 7분 풀이
    - number 의 길이가 매우 짧으므로 순열 사용해도 문제 없음
    - 소수 판별 함수만 작성해주면 쉽게 풀이 가능
    """
    from itertools import permutations

    def is_prime_number(x):
        is_prime = True if x > 1 else False
        for i in range(2, int(x ** (1 / 2)) + 1):
            if (x % i) == 0:
                return False

        return is_prime

    numbers = list(numbers)
    answer = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int("".join(p))
            if (num not in answer) and is_prime_number(num):
                answer.add(num)

    return len(answer)
