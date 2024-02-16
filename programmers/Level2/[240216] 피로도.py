"""
https://school.programmers.co.kr/learn/courses/30/lessons/87946
"""


def solution(k, dungeons):
    """
    - 약 5분 소요
    - 탐험 순서는 마음대로
    - 던전이 8개 이하이므로 순열로 완전탐색 가능!
    - 던전의 최소 피로도와 소모 피로도를 고려해 그리디하게 풀이도 가능할 것 같지만, 범위가 작으므로 완탐이 효율적
    """
    from itertools import permutations

    answer = -1

    all_dungeons = permutations(dungeons, len(dungeons))

    for dungeon in all_dungeons:
        tmp_k, tmp_ans = k, 0
        for limit, cost in dungeon:
            if tmp_k >= limit:
                tmp_k -= cost
                tmp_ans += 1
        answer = max(answer, tmp_ans)

    return answer
