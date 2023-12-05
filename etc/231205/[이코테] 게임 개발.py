"""
https://blex.me/@mildsalmon/chap-4-구현-게임-개발
"""


### 1st trial (time : 40m)
def try1():
    """
    - 주어진 상황들에 따라 시뮬레이션 -> 구현
    - 인덱스 에러가 나지 않도록 하는 22 ~ 24번째 코드를 나머지 연산 처리하면 한줄로 표현 가능
        - d = (d - 1) % 4
    """

    N, M = map(int, input().split())
    x, y, d = map(int, input().split())
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    board = [list(map(int, input().split())) for _ in range(N)]
    board[x][y] = 2  # 현재 좌표 방문 처리
    cnt, ans = 0, 0  # 회전 횟수, 방문 횟수

    while True:
        d -= 1  # 반시계방향 회전
        if d == -4:
            d = 0

        dx, dy = direction[d]  # 방향 변화 반영
        cnt += 1

        while board[x + dx][y + dy] == 0:  # 방문하지 않으면 계속 직진
            cnt = 0  # 회전 횟수 초기화
            ans += 1
            x += dx
            y += dy
            board[x][y] = 2  # 방문 처리

        if cnt == 4:  # 동서남북 다 회전해도 방문할 곳이 없었다면
            x -= dx  # 뒤로 가기
            y -= dy
            if board[x][y] == 1:  # 뒤로 가면 바다라면 종료
                break
            else:  # 바다가 아니라면 다시 시작
                ans += 1
                cnt = 0

    print(ans)


### solution
def solution():
    # N, M을 공백을 기준으로 구분하여 입력받기
    n, m = map(int, input().split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]
    # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
    x, y, direction = map(int, input().split())
    d[x][y] = 1  # 현재 좌표 방문 처리

    # 전체 맵 정보를 입력받기
    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    # 북, 동, 남, 서 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 왼쪽으로 회전
    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if array[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time = 0

    # 정답 출력
    print(count)


if __name__ == "__main__":
    try1()
