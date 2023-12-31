"""
https://www.acmicpc.net/problem/1074
"""


def solution():
    """
    - 약 40분 풀이 후 실패로 답지 참조
    - r행 c열을 몇 번째로 방문하는지 -> r행 c열의 숫자가 무엇인지
    - 4등분이 반복됨? -> 분할 정복/재귀

    - 답지 풀이
        - 좌표 r,c 가 2배가 됨에 따라 값이 4의 배수로 확장됨을 알 수 있음
            - ex) 14(2,3) -> 56(4,6)
            - ex) 8(2,0) -> 32(4,0)
        - 따라서 이 방식을 재귀 함수로 구현
            - 2 * (r % 2) + (c % 2) : 가장 작은 사분면 안에서 0,1,2,3 어디에 해당하는 지
            - 4 * sol(N - 1, int(r / 2), int(c / 2)) : 4의 배수하기 이전의 값
    """
    import sys

    input = sys.stdin.readline

    N, r, c = map(int, input().split())

    def sol(N, r, c):
        if N == 0:
            return 0

        return 2 * (r % 2) + (c % 2) + 4 * sol(N - 1, int(r / 2), int(c / 2))

    print(sol(N, r, c))


if __name__ == "__main__":
    solution()

"""
n = 2
"""
