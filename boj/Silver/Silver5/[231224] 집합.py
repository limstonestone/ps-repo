"""
https://www.acmicpc.net/problem/11723
"""


def try1():
    """
    - 약 5분 소요
    - set 자료형의 메소드를 아는지 묻는 문제, 주어진대로 따라가기
    """

    import sys

    input = sys.stdin.readline

    m = int(input())

    s = set()

    for _ in range(m):
        command = input().split()

        if len(command) > 1:
            command, num = command[0], int(command[1])
        else:
            command = command[0]

        if command == "add":
            s.add(num)

        elif command == "remove":
            s.discard(num)

        elif command == "check":
            print(1 if num in s else 0)

        elif command == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)

        elif command == "all":
            s = set(range(1, 21))

        elif command == "empty":
            s = set()


if __name__ == "__main__":
    try1()
