"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746#
"""


def solution(numbers):
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - sort 함수의 key 를 잘 정의해야함
        - 글자의 길이에 따라서 정렬 기준이 달라짐 -> 글자수를 통일해서 해결해보자 (4자리 이하)
        - "-" 등의 특수문자를 통해 글자수 통일, 근데 안풀림 ...

    - 답지 풀이
        - 글자수를 맞춰줄 때, 특정 숫자의 반복수열로
            - 34는 3과 30보다 앞으로 와야함
            - 3은 30보다 앞으로 와야함
            - 즉 다음 숫자가 무엇이 오냐가 정렬 기준이 될 수 있음
            - 동일한 자리수를 기준으로 비교하기 때문!
        - 예외처리 : [0,0,0,0] 의 경우 최종 답이 0이므로 int 변환 한번 필요함
    """

    numbers = sorted([str(x) for x in numbers], key=lambda x: x * 3, reverse=True)

    return str(int("".join(numbers)))  # 예외처리
