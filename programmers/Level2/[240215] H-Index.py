"""
https://school.programmers.co.kr/learn/courses/30/lessons/42747
"""


def solution(citations):
    """
    - 약 15분 소요
    - 정렬 후 이분 탐색을 활용해 큰 개수/ 적은 개수를 계산하여 조건을 만족시 최댓값으로 활용
    - 이분 탐색 없이 인덱싱으로도 풀이 가능
        - 발상 전환 : 조건 만족 논문 편수 h 를 찾기 -> 논문 중 가장 작은 인용수가 h 보다 큰지
    """
    import bisect

    citations.sort()
    n = len(citations)

    # 이분탐색
    for h in range(citations[-1], -1, -1):  # 위에서부터 내려오면 만족하자마자 최대값
        n_bigger = n - bisect.bisect_left(citations, h)
        if n_bigger >= h:
            return h

    # 인덱싱
    for i in range(n):
        if citations[i] >= n - i:  # n-i : h 를 의미
            return n - i

    return 0
