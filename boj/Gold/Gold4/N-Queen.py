"""
https://www.acmicpc.net/problem/9663
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 체스판에 퀸을 두고 같은 행,열,대각선에 있는지 확인하는 작업을 반복
        - 둔 퀸의 수가 n 이 되면 종료 -> 백트래킹

    - 답지 풀이
        - n x n 의 체스판에서 퀸이 N개이므로 한 행(열)에는 반드시 하나의 퀸만 옴
        - 따라서 행, 열 둘다 중복으로 확인할 필요 없이 행(또는 열)을 기준으로 탐색
            - 때문에 2차원 배열을 활용할 필요가 없음
        - 이후 대각선을 확인하는데, ↗ 대각선과 ↘ 대각선에 퀸 정보를 담은 배열 생성
            - 이 부분을 떠올리기가 힘들었던 것 같음 (1차원배열로 대각선 만들기)
    """

    n = int(input())
    check_col = [False] * n  # 같은 열에 다른 퀸이 있는지 확인하기 위한 배열
    check_dig = [False] * (
        2 * n - 1
    )  # ↗ 대각선을 확인하기 위한 배열: n x n 사각형의 대각선 개수는 (2*n-1)개
    check_dig2 = [False] * (
        2 * n - 1
    )  # ↘ 대각선을 확인하기 위한 배열: n x n 사각형의 대각선 개수는 (2*n-1)개

    def go(row: int) -> int:
        if row == n:  # 마지막 행까지 퀸을 모두 배치하면 종료
            return 1
        ans = 0  # (서로 공격할 수 없게) n개의 퀸을 놓을 수 있는 모든 경우의 수
        for col in range(n):  # (row, col)에 퀸을 놓기
            # 같은 열에 퀸이 있거나, ↗, ↘ 대각선에 퀸이 있는 경우 퀸을 둘 수 없음(가지치기)
            if check_col[col] or check_dig[row + col] or check_dig2[row - col]:
                continue
            check_col[col] = True  # (row, col)과 같은 열에 모든 칸에 퀸을 둘 수 없음
            check_dig[row + col] = (
                True  # (row, col)의 ↗ 대각선에 있는 모든 칸에 퀸을 둘 수 없음
            )
            check_dig2[row - col] = (
                True  # (row, col)의 ↘ 대각선에 있는 모든 칸에 더 이상 퀸을 둘 수 없음
            )
            ans += go(row + 1)

            # 해당 열에서의 경우의 수 계산이 끝났으니 퀸을 다시 회수(백트래킹)
            check_col[col] = False
            check_dig[row + col] = False
            check_dig2[row - col] = False

        return ans

    print(go(0))


if __name__ == "__main__":
    try1()
