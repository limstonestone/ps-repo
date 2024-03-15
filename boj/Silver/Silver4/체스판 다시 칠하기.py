"""
https://www.acmicpc.net/problem/1018
"""


def try1():
    """
    - 약 50분 소요
    - 주어진 입력 범위가 매우 작음 -> 시간복잡도 크게 신경쓰지 않아도 될 듯함
    - 8개씩 잘라서 일일히 확인해야하나? 규칙 먼저 탐색
        - 규칙은 파악하지 못했음, 입력 범위도 매우 작으므로 그냥 브루트 포스
    """
    import sys

    input = sys.stdin.readline
    n, m = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(n)]
    correct_board1, correct_board2 = [], []

    for _ in range(4):
        correct_board1.append(["B", "W"] * 4)
        correct_board1.append(["W", "B"] * 4)
        correct_board2.append(["W", "B"] * 4)
        correct_board2.append(["B", "W"] * 4)

    ans = int(1e9)

    for x in range((n - 8) + 1):
        tmp_board_x = board[x : x + 8]

        for y in range((m - 8) + 1):
            tmp_ans1, tmp_ans2 = 0, 0
            tmp_board = [board_x[y : y + 8] for board_x in tmp_board_x]

            for i in range(8):
                for j in range(8):
                    if tmp_board[i][j] != correct_board1[i][j]:
                        tmp_ans1 += 1
                    if tmp_board[i][j] != correct_board2[i][j]:
                        tmp_ans2 += 1
            ans = min(ans, tmp_ans1, tmp_ans2)

    print(ans)


if __name__ == "__main__":
    try1()
