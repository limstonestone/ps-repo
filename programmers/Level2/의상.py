"""
https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
"""


def solution(clothes):
    """
    - 약 50분 풀이 후 실패로 힌트 참조
    - 선택한 옷 종류만큼을 모두 더하지말고, 각 종류별로 입지 않았다는 옵션을 추가해주는 것이 훨씬 편리함
    """
    from collections import defaultdict

    dict_clothes = defaultdict(int)

    for name, cloth_type in clothes:
        dict_clothes[cloth_type] += 1

    answer = 1
    for cloth_type in dict_clothes:
        answer *= dict_clothes[cloth_type] + 1  # 선택하지 않았을 경우를 더해줌

    return answer - 1  # 모두 입지 않았을 때를 제외
