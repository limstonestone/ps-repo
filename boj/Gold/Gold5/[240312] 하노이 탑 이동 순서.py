"""
https://www.acmicpc.net/problem/11729
"""


def try1():
    """
    - 약 2시간 풀이 후 실패로 답지 참조
    - 답지 풀이
        - 하노이의 탑 자체에 대한 이해가 필요 (최소횟수가 보장되는 로직)
        - 어떻게 옮길지는 재귀를 활용하면 됨
        - 6 - start - end 에서 6의 의미:
            - 1,2,3 의 총합이 6이니 start 와 end 를 제외한 보조번호를 알 수 있음
    """
    import sys

    input = sys.stdin.readline

    n = int(input())

    def solve(n, start, end):
        if n == 1:
            print(start, end)
            return

        # 1 -> 2
        solve(n - 1, start, 6 - start - end)  # 가장 반경이 큰 원판을 제외한 탑을 2로
        # 1 -> 3
        print(start, end)  # 가장 반경이 큰 원판을 3으로
        # 2 -> 3
        solve(n - 1, 6 - start - end, end)  # 그동안 쌓은 탑을 반경이 큰 원판위로 올림

    print(2 ** (n) - 1)
    solve(n, 1, 3)


if __name__ == "__main__":
    try1()
