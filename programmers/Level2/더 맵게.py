"""
https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""


def solution(scoville, K):
    """
    - 약 10분 풀이
    - 최소 힙을 활용하여 풀이, 이 때 힙의 속성을 보장하기 위해 먼저 heapify 를 꼭 해주어야함
    """
    import heapq

    answer = 0
    heapq.heapify(scoville)

    while scoville:  # 계속해서 섞음
        min1 = heapq.heappop(scoville)
        if min1 >= K:  # 최소 값이 K 를 넘었으므로 정답값 리턴
            return answer
        if scoville:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
            answer += 1

    return -1  # 다 섞어도 조건에 미치지못했으므로 -1 리턴
