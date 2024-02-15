"""
https://school.programmers.co.kr/learn/courses/30/lessons/12909
"""


def solution(s):
    """
    - 약 4분 소요
    - "(" 를 스택에 저장해두고있다가, ")" 를 만났을 때 "(" 를 스택에서 제거하면 됨
        - 이 때, 숫자가 안맞는 현상 발생시 정답은 False 가 될 것
    """
    stack = []
    answer = True

    for tmp_s in s:
        if tmp_s == ")":
            if stack:  # 스택이 비어있다면, 즉 ")" 가 더 많은 현상
                stack.pop()
            else:
                answer = False
                break
        else:
            stack.append("(")

    if stack:  # 최종적으로 스택이 남아있다면, 즉 "(" 가 더 많은 현상
        answer = False

    return answer
