"""
https://www.acmicpc.net/problem/5397
"""


def try1():
    """
    - 약 5분 소요
    - 문자열의 길이가 100만 -> O(NlogN)
    - 커서 문제 -> 왼쪽, 오른쪽 deque 을 선언한 후 풀이하면 편리
    """

    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        password = input().rstrip()
        left, right = deque(), deque()
        for pw in password:
            if pw == "<":
                if left:
                    right.appendleft(left.pop())
            elif pw == ">":
                if right:
                    left.append(right.popleft())
            elif pw == "-":
                if left:
                    left.pop()
            else:
                left.append(pw)

        print("".join(list(left) + list(right)))


if __name__ == "__main__":
    try1()
