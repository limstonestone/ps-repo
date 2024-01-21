"""
https://www.acmicpc.net/problem/9655
"""


def try1():
    """
    - 약 10분 소요
    - 베스킨라빈스31 게임을 생각해보면, 특정 패턴 마다 이기는 사람이 정해져있음
    - 가져가는 돌의 수가 홀 수이고 상근이가 먼저 시작
        - 돌이 홀 수개면 상근 승리 (홀 + 홀 + 홀 = 홀)
        - 돌이 짝 수개면 창영 승리 (홀 + 홀 = 짝)
        - 즉, 상근이의 턴이 홀 수 턴, 창영이의 턴은 짝 수 턴임에 근거
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    print("SK" if n % 2 == 1 else "CY")


if __name__ == "__main__":
    try1()
