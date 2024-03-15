"""
https://www.acmicpc.net/problem/1406
"""


def try1():
    """
    - 약 20분 소요
    - 커서를 기준으로 왼쪽 배열, 오른쪽 배열을 각각 변수로 저장
    - 이후 deque 자료구조를 활용하여 편리하게 삽입/삭제를 왼쪽/오른쪽에서 활용
    """

    import sys
    from collections import deque

    input = sys.stdin.readline

    seq = list(input().rstrip())
    M = int(input())
    right = deque()

    for _ in range(M):
        command = input().rstrip()

        if command == "L":
            if seq:
                right.appendleft(seq.pop())
        if command == "B":
            if seq:
                seq.pop()
        if command == "D":
            if right:
                seq.append(right.popleft())

        if "P" in command:
            seq.append(command[-1])

    print("".join(seq + list(right)))


if __name__ == "__main__":
    try1()
