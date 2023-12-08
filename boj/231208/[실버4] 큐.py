"""
https://www.acmicpc.net/problem/10845
"""


def try1():
    """
    - 약 20분 소요
    - queue 구현 -> deque 활용
    - 커맨드가 맞는지 확인할 때, 등호로 확인하면 띄어쓰기가 포함되는 경우가 있으므로 in 연산으로 처리
    """
    from collections import deque

    import sys

    input = sys.stdin.readline

    N = int(input())
    queue = deque()

    for _ in range(N):
        command = input()

        if "pop" in command:
            print(-1) if not queue else print(queue.popleft())

        elif "size" in command:
            print(len(queue))

        elif "empty" in command:
            print(1) if not queue else print(0)

        elif "front" in command:
            print(-1) if not queue else print(queue[0])

        elif "back" in command:
            print(-1) if not queue else print(queue[-1])

        else:  # push
            commands = command.split()
            command, num = commands[0], int(commands[1])

            queue.append(num)


if __name__ == "__main__":
    try1()
