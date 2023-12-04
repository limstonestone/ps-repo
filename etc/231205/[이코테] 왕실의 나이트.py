"""
https://blex.me/@mildsalmon/chap-4-구현-왕실의-나이트
"""


### 1st trial (time : 10m)
def try1():
    """
    - 최대 경우의수 8, 최소 경우의 수 2(아마도?)로서 범위가 작음 -> 구현
    - 범위가 작으므로 하드코딩하면 조금 지저분하지만 쉽게 풀이 가능

    """
    abc2int = dict(zip("abcdefgh", range(1, 9)))
    col, row = input()
    col, row = abc2int[col], int(row)

    ans = 0
    if (col - 2) > 0:
        if (row - 1) > 0:
            ans += 1
        if (row + 1) < 9:
            ans += 1
    if (col + 2) < 9:
        if (row - 1) > 0:
            ans += 1
        if (row + 1) < 9:
            ans += 1
    if (col + 1) < 9:
        if (row - 2) > 0:
            ans += 1
        if (row + 2) < 9:
            ans += 1
    if (col - 1) > 0:
        if (row - 2) > 0:
            ans += 1
        if (row + 2) < 9:
            ans += 1

    print(ans)


### solution
def solution():
    """
    - 8가지 방향이 정해져있으므로 하드코딩 대신 반복문 사용
    - 또한 dictionary 대신 ASCII 코드를 활용한 ord() 내장함수 사용 가능

    """
    input_data = input()
    row = int(input_data[1])
    col = int(ord(input_data[0])) - int(ord("a")) + 1

    # 나이트 이동 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    ans = 0
    for step in steps:
        next_row, next_col = row + step[0], col + step[1]
        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            ans += 1

    print(ans)


if __name__ == "__main__":
    try1()
