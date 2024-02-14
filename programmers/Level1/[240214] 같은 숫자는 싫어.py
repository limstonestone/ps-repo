"""
https://school.programmers.co.kr/learn/courses/30/lessons/12906
"""


def solution(arr):
    """
    - 약 5분 소요
    - 인접한 숫자를 인덱싱으로 확인 후 더하는 작업을 수행
    """
    answer = [
        -1
    ]  # 0~9 사이의 숫자가 주어지므로 무시되는, 인덱싱 오류를 방지하기 위한 숫자
    i = 1
    for x in arr:
        if answer[i - 1] != x:
            answer.append(x)
            i += 1

    return answer[1:]
