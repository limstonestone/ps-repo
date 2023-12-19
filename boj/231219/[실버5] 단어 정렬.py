"""
https://www.acmicpc.net/problem/1181
"""


def try1():
    """
    - 1037
    - 입력 범위 충분 -> 파이썬 라이브러리로 정렬
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    sequence = [input().rstrip() for _ in range(n)]
    sequence = list(set(sequence))

    sequence.sort()
    tmp_list = [0] * len(sequence)
    for i in range(len(sequence)):
        tmp_list[i] = (i, sequence[i])

    tmp_list.sort(key=lambda x: (len(x[1]), x[0]))

    for seq in tmp_list:
        print(seq[1])


def solution():
    """
    - 더 나은 풀이
    - 사전식으로 먼저 정렬을 해버리면 사실 길이순으로 뒤에 정렬을 하더라도 문제가 없게 정렬이 됨
    """
    n = int(input())

    words = [str(input()) for i in range(n)]

    words = list(set(words))
    words.sort()
    words.sort(key=len)

    for i in words:
        print(i)


if __name__ == "__main__":
    try1()
