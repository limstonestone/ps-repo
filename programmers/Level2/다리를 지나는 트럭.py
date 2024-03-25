"""
https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""


def solution(bridge_length, weight, truck_weights):
    """
    - 약 1시간 소요
    - 동시에 다리를 건너는 트럭이 많을 수록 좋음, 즉 정해진 무게만큼 꽉꽉 채워서 가야함
    - 병렬적으로 움직이는 현상을 구현하기에는 굉장히 복잡하며 효율성 문제 발생할 수 있음
        - 따라서 다리의 상태를 구현하여 1초마다 다리의 맨 왼쪽 트럭을 건너게하는 방식으로 구현
        - 그 과정에서 deque 을 활용하여 효율적으로 append, pop
    """
    from collections import deque

    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 다리의 트럭 상태, 0으로 초기화
    bridge_weights = 0  # 다리의 현재 무게 상태

    while bridge:
        answer += 1  # 1초가 흐름
        done = bridge.popleft()  # 다리의 가장 왼쪽 트럭을 건너게 함
        bridge_weights -= done  # 트럭이 건넜으므로 그만큼 다리 무게 빼줌

        if truck_weights:
            while len(bridge) < bridge_length:  # 다리 최대 길이를 넘지 않을때까지 반복
                truck = truck_weights.popleft()  # 트럭을 순서대로 차출
                if bridge_weights + truck <= weight:  # 무게를 초과하지 않는다면 추가
                    bridge.append(truck)
                    bridge_weights += truck
                else:  # 초과한다면 도로 넣어놓고 해당 시간에는 아무일이 일어나지 않음 -> 0 추가
                    truck_weights.appendleft(truck)
                    bridge.append(0)

    return answer
