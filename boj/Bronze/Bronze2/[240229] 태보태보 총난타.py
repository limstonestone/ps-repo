"""
https://www.acmicpc.net/problem/17249
"""


def try1():
    """
    - 약 3분 소요
    - 입력의 길이가 1000 이하 -> O(N^2) 미만으로 풀이
    - 가장 직관적으로 시작부터 끝까지 탐색 -> O(N)
        - 주먹을 마주치면 count 증가
        - 얼굴을 만나면 기존 count 왼쪽값, 오른쪽으로 다시 count
    """
    import sys

    input = sys.stdin.readline
    taebo = input().rstrip()
    cnt = 0
    for x in taebo:
        if x == "@":
            cnt += 1
        if x == "(":
            left = cnt
            cnt = 0

    right = cnt
    print(left, right)


if __name__ == "__main__":
    try1()
