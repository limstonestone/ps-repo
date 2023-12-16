"""
https://www.acmicpc.net/problem/19583
"""


def try1():
    """
    - 약 20분 소요
    - 채팅기록이 최대 10만 -> O(NlogN)
    - 계산 상 편의를 위해 전부 분 단위로 변환
        - 이름이 있는지 없는지 확인하는 작업 시 set 자료형을 활용하여 O(1) 시간복잡도로 연산

    """

    import sys

    input = sys.stdin.readline

    def h2m(x):  # hh:mm 형식
        return 60 * int(x[:2]) + int(x[3:])

    S, E, Q = list(map(h2m, input().split()))
    answer = 0

    entry_list = set()

    for _ in range(100000):  # 최대 10만 줄
        chat = input().split()
        if chat:
            time, name = h2m(chat[0]), chat[1]
            if time <= S:
                entry_list.add(name)

            elif E <= time <= Q:
                if name in entry_list:
                    entry_list.discard(name)
                    answer += 1
        else:  # 입력이 주어지지 않을 때 반복문 멈춤
            break

    print(answer)


if __name__ == "__main__":
    try1()
