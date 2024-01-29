"""
https://www.acmicpc.net/problem/5430
"""


def try1():
    """
    - 약 35분 소요
    - 자료구조를 잘 활용하여 시간복잡도를 최대한 줄인 로직을 구현하기
    - 버리는 것은 문제가 크게 없지만, 뒤집는 것에서 시간을 줄이는 것이 관건
        - 현재가 뒤집힌 상태인지, 아닌지를 알고 있다면 배열을 계속 뒤집을 필요없이 앞 뒤에서 빼면 됨
        - 또한 deque 을 활용하여 좌/우 삭제를 시행
    - n = 0 일 때의 반례를 주의해야함
    """
    import sys
    from collections import deque

    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        p = input().rstrip()
        n = int(input())

        arr = input().rstrip()[1:-1].split(",")
        arr = deque(map(int, arr)) if arr != [""] else []
        status, ans = True, True

        for p in p:
            if p == "R":
                status = False if status else True

            else:
                if arr:
                    # 현재 상태에 따른 좌 / 우 삭제
                    arr.popleft() if status else arr.pop()
                else:
                    print("error")  # 배열이 비어있는데 D 작업
                    ans = False  # 정답은 출력하지 않음
                    break

        if not status:  # 마지막 상태가 역방향이라면 뒤집기
            arr.reverse()

        if ans:  # 에러가 없었다면
            print(str(list(arr)).replace(" ", ""))


if __name__ == "__main__":
    try1()
