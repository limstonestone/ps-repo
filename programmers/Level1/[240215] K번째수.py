"""
https://school.programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    """
    - 약 3분 소요
    - 입력의 범위가 매우 작으므로 단순 슬라이싱/인덱싱 활용
    """
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1 : j])[k - 1])
    return answer
