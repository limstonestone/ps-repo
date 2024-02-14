"""
https://school.programmers.co.kr/learn/courses/30/lessons/42576
"""


def solution(participant, completion):
    """
    - 약 7분 소요
    - collections 모듈의 Counter 도 이용할 수 있지만, 라이브러리 사용은 자제해보려했음
    - 따라서 정렬 이후 순차적으로 비교하는 방식을 채택
    """
    participant.sort()
    completion.sort()
    answer = participant[-1]  # 정렬 시 맨 마지막 원소가 정답일 경우

    for i, name in enumerate(completion):
        if participant[i] != name:
            answer = participant[i]
            break

    return answer
