"""
https://www.acmicpc.net/problem/1107
"""


def try1():
    """
    - 240126) 약 1시간 30분 풀이 후 첫 실패 -> 힌트 참고
    - 240129) 약 20분 소요

    - 처음에는 글자 수(단위)에 맞춰서 하나하나 필터링하는 경우를 생각했지만, 반례들이 많이 존재함
        - 10000 의 경우 -> 9999 + 1 이 나은 경우가 있을 수 있음
    - 따라서 가능한 전체 채널에 대해 모두 구한 다음 최소값으로 결정
        - 시간 복잡도 계산 시 O(N)이면 충분하기 때문
        - 위에서 아래로 내려오는 경우도 있으므로, N이 5만이니 최대 10만까지 서치
    - ans = min(ans, abs(n - num) + len(str(num)))
        - 현재 채널(100)에서 위, 아래버튼만 누르기 vs 특정 번호로 이동한다음 위아래버튼 누르기
    - 반례가 너무 복잡하다면 단순한 방법, 완전 탐색으로 생각해보기! 오히려 더 빨리 해결할 수 있음


    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    m = int(input())
    crashed = set(map(int, input().split())) if m != 0 else []

    ans = abs(n - 100)

    for num in range(1_000_001):
        status = True

        for i in str(num):
            if int(i) in crashed:
                status = False
                break

        if status:
            ans = min(ans, abs(n - num) + len(str(num)))

    print(ans)


if __name__ == "__main__":
    try1()
