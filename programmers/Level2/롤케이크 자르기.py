"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""


def solution(topping):
    """
    - 약 20분 소요
    - 입력 크기 최대 100만 -> O(N) ~ O(logN)
    """
    from collections import Counter

    left, right = set(), dict(Counter(topping))
    left_cnt, right_cnt = 0, len(right)
    idx, cnt = 0, 0

    while True:
        if (
            topping[idx] not in left
        ):  # 왼쪽 커팅에 들어있지 않으면 (새로운 토핑 발견되면)
            left.add(topping[idx])  # 집합에 추가
            left_cnt += 1  # 시간복잡도를 위해 상수로 선언, 왼쪽 토핑 개수 +1

        right[topping[idx]] -= 1  # 오른쪽에 해당 토핑의 cnt 값 -1

        if right[topping[idx]] == 0:  # cnt==0 -> 오른쪽에 해당 토핑이 존재하지 않음
            right_cnt -= 1  # 오른쪽 토핑 개수 -1

        if left_cnt == right_cnt:  # 왼쪽 토핑 개수와 오른쪽이 같다면 정답 +1
            cnt += 1

        if (
            left_cnt > right_cnt
        ):  # 왼쪽 토핑개수가 오른쪽보다 많아진다면 더이상 탐색할 필요 X
            break

        idx += 1

    return cnt
