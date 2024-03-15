"""
https://www.acmicpc.net/problem/2164
"""


def try1():
    """
    - 약 5분 소요
    - N 의 범위가 최대 50만 -> O(NlogN) ~ O(N)
    - deque 를 활용하여 좌/우, 삽입/추출 을 편하게 가능
    """
    from collections import deque

    N = int(input())
    cards = deque([x for x in range(1, N + 1)])  # 1,...,N

    while True:
        bottom1 = cards.popleft()  # 제일 위 카드 버리기
        if not cards:
            break
        bottom2 = cards.popleft()  # 제일 위 카드 제일 아래로 옮기기
        cards.append(bottom2)

    print(bottom1)


if __name__ == "__main__":
    try1()
