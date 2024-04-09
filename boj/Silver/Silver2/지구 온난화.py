"""
https://www.acmicpc.net/problem/5212
"""


def try1():
    """
    - 약 20분 소요
    - 반례가 조금 이상하다 생각해 문제를 잘 읽어보니 바다의 모서리 부분들은 전부 .으로 채워져있음 (입력 범위를 넘어가더라도)
    """
    import sys
    from copy import deepcopy

    input = sys.stdin.readline
    row, col = map(int, input().split())

    # 테두리 처리
    graph = [["."] + list(input().rstrip()) + ["."] for _ in range(row)]
    graph = [["."] * (col + 2)] + graph
    graph = graph + [["."] * (col + 2)]

    answer = deepcopy(graph)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 테두리 처리 이후 인덱스가 증가해야함
    row += 2
    col += 2

    def check_condition(x, y):  # 잠기는 지 확인
        cnt = 0
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == ".":
                cnt += 1
        return True if cnt >= 3 else False

    min_row, max_row, min_col, max_col = row, 0, col, 0

    for r in range(row):
        for c in range(col):
            if graph[r][c] == "X":
                if check_condition(r, c):
                    answer[r][c] = "."
            if answer[r][c] == "X":  # 살아있는 섬의 사이즈 확인
                min_row, min_col = min(r, min_row), min(c, min_col)
                max_row, max_col = max(r, max_row), max(c, max_col)

    for ans_row in answer[min_row : max_row + 1]:
        print("".join(ans_row[min_col : max_col + 1]))


if __name__ == "__main__":
    try1()
