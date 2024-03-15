"""
https://school.programmers.co.kr/learn/courses/30/lessons/76502
"""


def solution(s):
    """
    - 약 15분 소요
    - 입력 길이 1000이하 -> O(N^2) 까지도 가능
    """
    from collections import deque

    answer = 0
    s = deque(s)
    match = {")": "(", "]": "[", "}": "{"}

    for _ in range(len(s)):
        status = True
        stack = []
        for x in s:
            if x in ["(", "[", "{"]:
                stack.append(x)
            else:
                if stack:
                    if (
                        stack.pop() != match[x]
                    ):  # 알맞은 쌍이 직전에 나오지 않았다면 중단
                        status = False
                        break
                else:  # "(", "[", "{" 가 사전에 나오지 않았다면 바로 중단
                    status = False
                    break
        if status:
            if not stack:
                answer += 1

        s.append(s.popleft())

    return answer
