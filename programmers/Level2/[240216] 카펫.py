"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""


def solution(brown, yellow):
    """
    - 약 15분 풀이
    - 가로 길이가 더 김 -> 경우의 수가 절반으로 줄어드는 것과 마찬가지 -> 완전탐색
    - 전체 넓이 = brown + yellow
    - 테두리가 1줄이 고정이므로, yellow 의 개수는 (가로 - 2) * (세로 - 2)
    - 또한 전체에서 세로(가로)를 나누었을 때 나머지가 0이어야함
    """
    total = brown + yellow

    h = 1
    while h <= total // h:
        if (total % h == 0) and ((h - 2) * (total // h - 2) == yellow):
            answer = [total // h, h]
        h += 1

    return answer
