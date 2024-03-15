"""
https://www.acmicpc.net/problem/10866
"""


def try1():
    """
    - 약 10분 소요
    - deque 자료형으로 다 해결가능
    - startswith 메소드로 입력에 띄어쓰기 등이 포함되었을 때 문제를 해결
    """
    from collections import deque

    import sys

    input = sys.stdin.readline

    N = int(input())
    queue = deque()

    for _ in range(N):
        command = input()

        if command.startswith("pop_front"):
            print(-1) if not queue else print(queue.popleft())

        elif command.startswith("pop_back"):
            print(-1) if not queue else print(queue.pop())

        elif command.startswith("size"):
            print(len(queue))

        elif command.startswith("empty"):
            print(1) if not queue else print(0)

        elif command.startswith("front"):
            print(-1) if not queue else print(queue[0])

        elif command.startswith("back"):
            print(-1) if not queue else print(queue[-1])

        else:  # push
            commands = command.split()
            command, num = commands[0], int(commands[1])

            if "push_front" in command:
                queue.appendleft(num)
            elif "push_back" in command:
                queue.append(num)


if __name__ == "__main__":
    try1()
