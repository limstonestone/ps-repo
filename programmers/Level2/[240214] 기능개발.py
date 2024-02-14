"""
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""


def solution(progresses, speeds):
    """
    - 약 10분 소요
    - 큐를 활용하여, 첫번째 기능이 배포될때까지 계속해서 작업 진행
    - 이후 첫번째 기능이 배포된다면, 이후 작업들도 배포가능한 것들을 계속해서 배포 (popleft)
    """
    from collections import deque

    answer = []
    progresses, speeds = deque(progresses), deque(speeds)

    while progresses:
        tmp_ans = 0
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            tmp_ans += 1
            if not progresses:
                break

        answer.append(tmp_ans)

    return answer
