"""
https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""


def solution(answers):
    """
    - 약 10분 소요
    - 배열을 굳이 만들 필요 없이 나머지 연산을 통한 인덱싱으로 O(n) 으로 비교 가능
    """
    scores = [0, 0, 0]

    for i, ans in enumerate(answers):
        scores[0] += [1, 2, 3, 4, 5][i % 5] == ans
        scores[1] += [2, 1, 2, 3, 2, 4, 2, 5][i % 8] == ans
        scores[2] += [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][i % 10] == ans

    answer = []
    for i, ans in enumerate(scores):
        if ans == max(scores):
            answer.append(i + 1)
    return answer
