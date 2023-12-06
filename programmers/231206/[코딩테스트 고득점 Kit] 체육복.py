"""
https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
"""


def solution1(n, lost, reserve):
    """
    - 약 20분 소요
    - 여벌이 있는 사람이 빌려줌, 인접한 학생에게만 빌려줄 수 있음, 여벌은 하나만
    - 최대한 체육복이 없는 사람이 없도록 여벌 체육복이 있는 사람들이 배분해주어야함
    - n 은 최대 30 -> O(N^3) 까지도 가능
    - 우선 먼저 여벌이 있는데 도난 당한 경우를 처리해야 문제가 덜 복잡해짐
        - 차집합으로 처리
    """

    set_lost = set(lost).difference(reserve)
    set_reserve = set(reserve).difference(lost)

    answer = n - len(set_lost)

    for lost in set_lost:
        if lost - 1 in set_reserve:
            set_reserve.discard(lost - 1)
            answer += 1

        elif lost + 1 in set_reserve:
            set_reserve.discard(lost + 1)
            answer += 1

    return answer
