"""
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""


def solution(people, limit):
    """
    - 약 1시간 소요
    - 최대한 작은 사람끼리 묶어서 보내다가 한 사람이 무게 제한을 넘는 순간부터 보트는 한 개씩 필요
        - 인 줄 알았지만 [1,2,3,4], 5 와 같은 경우 [1,4], [2,3] 묶음으로 보내는 것이 정답
    - 구명보트는 한번에 2명씩 밖에 타지 못함
        - 이 조건을 놓치니 문제가 굉장히 복잡해짐
    - 이분탐색으로 접근했지만 정확히는 투포인터인 문제
        - 이분탐색 풀이 시 deque 를 사용하지 않으면 하나의 테스트케이스가 시간초과 발생
    """
    import bisect
    from collections import deque

    answer = 0
    people = deque(sorted(people))

    # 이분탐색
    while people:
        weight = people.pop()

        if people and limit - weight >= people[0]:
            idx = bisect.bisect(people, limit - weight)
            del people[idx - 1]

        answer += 1

    # 투포인터
    answer = len(people)
    left, right = 0, answer - 1

    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            answer -= 1  # 두 명을 태움
        right -= 1

    return answer
