"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    """
    - 약 2분 소요
    - 고를 수 있는 폰켓몬들 중 겹치는 폰켓몬이 적을 수록 좋음 -> 집합 활용
    """
    return min(len(nums) // 2, len(set(nums)))
