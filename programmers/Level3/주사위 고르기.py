"""
https://school.programmers.co.kr/learn/courses/30/lessons/258709
"""


def solution(dice):
    """
    - 약 2시간 풀이 후 힌트 참조
    - 승리할 확률이 가장 높은 주사위 조합은 유일함 -> 완전탐색으로 풀이
    - Product + Combination 을 활용해 가능한 쌍을 구할 수 있음
    - 경우의수 그대로 구현 후 완전탐색 시 시간초과 발생, 중복되는 계산을 해결해야 함
        - 리스트B를 정렬 + 이분탐색을 활용해서 승리 경우의수를 O(logN) 으로 구함
        - 정렬하고 나면 특정 cutoff 이후의 값들은 모두 패배가 되기 때문
    """
    from itertools import combinations as C
    from itertools import product as P
    from bisect import bisect_left

    n = len(dice)
    max_win = -1

    for case_a in C(range(1, n + 1), n // 2):
        case_b = set(range(1, n + 1)) - set(case_a)

        # 가능한 모든 경우의 주사위들을 던져 나온 수의 합
        result_a = [sum(x) for x in P(*[dice[x - 1] for x in case_a])]
        result_b = [sum(x) for x in P(*[dice[x - 1] for x in case_b])]
        result_b.sort()

        # 이분탐색의 인덱스 -> 승리한 수
        win_count_a = sum(bisect_left(result_b, num) for num in result_a)

        # 최대 승리를 가진다면 갱신
        if win_count_a > max_win:
            max_win = win_count_a
            answer = case_a

    return answer
