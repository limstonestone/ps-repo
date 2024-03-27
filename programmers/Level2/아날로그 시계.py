"""
https://school.programmers.co.kr/learn/courses/30/lessons/250135
"""


def solution(h1, m1, s1, h2, m2, s2):
    """
    - 약 3시간 소요

    - 우선 시계 한바퀴돌면 초기화가 필요하므로 각 침의 각도를 통해서 로직 구현 가능
    - 초침 속도가 가장 빠르므로 초침이 앞에있다가 역전당하는 일은 없음
    - 12시침 근처에서 엣지 발생 -> 나머지로 보완
        - 예를 들어 초침이 358 도였다가 1도가 되는 순간 시침이 359도인 상황을 주의해야함
        - 또한 이는 넘어가는 상황에서만 발생

    - continuous한 움직임을 어떻게 discrete하게 쪼갤것?
        - 애초에 정확하게 같은 값을 찾을 수 있나?
            - 예제에서 전부 소수점 세자리에서 겹치는 것이 의미하는 것이 있나? -> 못찾겠음
        - 정확하게 같은 값을 찾는 것은 불가능할 듯함
        - -> 초침이 시침/분침의 이전 값에있다가 다음 텀에 그 값을 초과한다면 겹친적이 있는 것

    - 초침이 시침/분침 두개랑 겹쳐도 한번만 알람이 울리는 것 주의해야할 듯함
        - 각도를 계속해서 누적한다면 부동소수점 오차 때문에 위 경우가 계산이 안됨
            - 시작시간 - 종료시간을 초로 계산하여 반복문마다 1초씩 빼면서 각도를 쌓아가는 로직
            - 테스트케이스 1개 통과 X (하루종일 디버깅하다가 실패 ㅠㅠㅠ)
        - 따라서 루프마다 현재 시간에 따라서 각도를 새로 구해야함
    """
    # 1초당 움직이는 각도
    s_ang_unit = 6
    m_ang_unit = s_ang_unit * (1 / 60)
    h_ang_unit = m_ang_unit * (1 / 12)

    def h2s(h1, m1, s1):
        return 60 * 60 * h1 + 60 * m1 + s1

    start_time, end_time = h2s(h1, m1, s1), h2s(h2, m2, s2)

    def init_(x):  # 각도가 360도를 넘을 때 초기화, 이 때 딱 360도면 360으로 변환해야함
        return 360 if x % 360 == 0 else x % 360

    # 자정이나 오후 12시일 경우 겹치고 시작
    answer = 1 if start_time in (0, 12 * 3600) else 0

    for now in range(start_time, end_time):
        s_ang_now = ((now * s_ang_unit)) % 360
        m_ang_now = ((now * m_ang_unit)) % 360
        h_ang_now = ((now * h_ang_unit)) % 360

        s_ang_nxt = init_((now + 1) * s_ang_unit)  # 360 -> 0이 안되게 init 함수 적용
        m_ang_nxt = init_((now + 1) * m_ang_unit)
        h_ang_nxt = init_((now + 1) * h_ang_unit)

        if s_ang_now < m_ang_now and s_ang_nxt >= m_ang_nxt:
            answer += 1

        if s_ang_now < h_ang_now and s_ang_nxt >= h_ang_nxt:
            answer += 1

        if s_ang_nxt == m_ang_nxt == h_ang_nxt:  # 시침 분침 초침이 다 같을 때 중복 제거
            answer -= 1

    return answer
