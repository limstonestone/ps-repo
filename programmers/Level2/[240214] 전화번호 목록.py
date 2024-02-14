"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""


def solution(phone_book):
    """
    - 약 5분 소요
    - 접두사이므로 startswith 함수를 사용, 이 때 정렬을 해준다면 인접 원소들끼리만 비교해줘도 됨
    """
    n = len(phone_book)
    phone_book.sort()
    answer = True
    i = 0

    while i < n - 1:
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break
        else:
            i += 1
    return answer
