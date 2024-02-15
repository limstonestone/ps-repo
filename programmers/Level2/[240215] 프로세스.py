def solution(priorities, location):
    """
    - 약 1시간 풀이
    - 전형적인 큐의 프로세스
    - 입력의 크기가 100이므로 이중반복문을 사용하더라도 문제 없음
    - 프로세스를 실행시키지않고(즉 큐에서 삭제시키지않고) 큐의 왼편에 계속 둘 경우 문제가 생김을 주의
        - 해당 시점의 큐의 상태에서 변화가 일어나지 않음
    """
    from collections import deque

    q = deque([(i, priority) for i, priority in enumerate(priorities)])
    answer = 0

    while True:
        i, cur_priority = q.popleft()
        stop_flag = True
        for j, priority in q:
            if priority > cur_priority:  # 뒤에 더 큰 우선순위가 있을 경우
                q.append((i, cur_priority))  # 맨 뒤로 보냄
                stop_flag = False
                break  # 굳이 더 볼 필요없으므로 반복문 중단

        if stop_flag:  # 더 큰 우선순위가 없을 경우
            answer += 1  # 프로세스 실행시켜버림 (큐에서도 삭제됨)
            if i == location:
                return answer
