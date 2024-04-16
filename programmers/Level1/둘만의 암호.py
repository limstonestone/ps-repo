"""
https://school.programmers.co.kr/learn/courses/30/lessons/155652
"""


def solution(s, skip, index):
    """
    - 약 5분 소요
    """
    import string

    alphabet = string.ascii_lowercase  # 알파벳 배열 선언
    k = len(alphabet)
    answer = ""

    for x in s:
        idx = alphabet.index(x) + 1  # 현재 알파벳이 존재하는 인덱스 반환
        cnt = 0

        while cnt < index:  # index 만큼 뒤로 탐색 시작
            idx = 0 if idx >= k else idx  # z 를넘어가면 a로 다시 회귀

            if alphabet[idx] not in skip:  # skip 에 없다면 탐색으로 포함
                cnt += 1

            idx += 1

        answer += alphabet[idx - 1]  # 조건을 만족하는 탐색이 끝난 문자 추가

    return answer
