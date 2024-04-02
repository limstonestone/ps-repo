"""
https://school.programmers.co.kr/learn/courses/30/lessons/147355
"""


def solution(t, p):
    """
    - 약 2분 소요
    - p와 t의 길이가 최대 1만 -> O(N^2) 으로는 힘들어보임
    """
    answer = 0
    len_p = len(p)  # 반복문 마다 p의 길이를 구하는 것은 효율적이지 X
    p = int(p)  # p는 정수로 바로 반환해버려도 문제 없음, 사전에 반환

    for i in range(len(t) - len_p + 1):
        if int(t[i : i + len_p]) <= p:
            answer += 1

    return answer


def solution(t, p):
    """
    - 재귀 풀이
    """
    import sys

    sys.setrecursionlimit(int(1e9))
    answer = 0

    len_p = len(p)  # 반복문 마다 p의 길이를 구하는 것은 효율적이지 X
    p = int(p)  # p는 정수로 바로 반환해버려도 문제 없음, 사전에 반환

    def recursive(idx):
        nonlocal answer
        if idx == len(t) - len_p + 1:
            return
        if int(t[idx : idx + len_p]) <= p:
            answer += 1
        recursive(idx + 1)

    recursive(0)

    return answer
