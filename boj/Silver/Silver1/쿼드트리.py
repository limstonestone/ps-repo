"""
https://www.acmicpc.net/problem/1992
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 힌트 참조
    - 완전탐색을 하되 특정 조건이 있을 때 종료 -> 백트래킹
    - 사각형을 네개로 쪼갠 후 왼쪽 위,오른쪽 위,왼쪽 아래,오른쪽 아래 반복 탐색
        - 이 때 모두가 0이나 1로 이루어져있는 경우 탐색 종료
            - 이를 위해 네모 그래프의 모든 값을 직접탐색 (입력 길이가 작으니 상관X)
        - 즉 사각형 한 개 짜리가 들어오는 경우도 포함
    - 그래프를 직접 쪼개는 것이 아니라, 좌표로 접근해야 훨씬 수월함
    """
    import sys

    sys.setrecursionlimit(987654321)

    input = sys.stdin.readline

    n = int(input())
    graph = [input().rstrip() for _ in range(n)]

    answer = ""

    def divide(size, r, c):
        nonlocal answer
        tmp_value = graph[r][c]

        # 주어진 네모의 주변을 탐색
        for x in range(r, r + size):
            for y in range(c, c + size):
                if tmp_value != graph[x][y]:
                    tmp_value = -1  # 더 나누어야 함
                    break

        if tmp_value == -1:  # 더 나누어야한다면, 왼쪽 위 ~ 오른쪽 아래 순서로 쪼개기
            answer += "("  # 나누었다는 걸 표시
            divide(size // 2, r, c)
            divide(size // 2, r, c + size // 2)
            divide(size // 2, r + size // 2, c)
            divide(size // 2, r + size // 2, c + size // 2)
            answer += ")"

        else:  # 더 안나누고 값이 하나만 나온다면 정답으로 추가
            answer += tmp_value

    divide(n, 0, 0)
    print(answer)


if __name__ == "__main__":
    try1()
