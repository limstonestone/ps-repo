"""
https://www.acmicpc.net/problem/10828
"""


def try1():
    """
    - 약 4분 소요
    - 주어진 대로 스택 잘 구현하기
    """

    import sys

    input = sys.stdin.readline

    n = int(input())
    stack = []

    for _ in range(n):
        command = input().rstrip()
        if "push" in command:
            command = command.split()
            stack.append(command[1])
        elif command == "pop":
            print(stack.pop() if stack else -1)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            print(0 if stack else 1)
        elif command == "top":
            print(stack[-1] if stack else -1)


if __name__ == "__main__":
    try1()
