"""
https://www.acmicpc.net/problem/1946
"""


def try1():
    """
    - 약 18분 소요
    - n이 최대 10만 -> O(NlogN)으로 해결해야 함
    - 둘 다 비교해야하는 것 처럼 보이지만, 사실 면접과 서류 둘 중 하나의 기준으로 정렬을 해놓으면 다른 하나만 비교하면 됨
        - 예를 들어 서류 기준으로 정렬을 하면 아래와 같음
            - (1,3), (2,2), (3,1)
        - 반복문을 통해 뒤로 탐색할수록 서류 등수가 떨어지는 건 당연하므로, 면접 등수가 더 높은지만 확인하면 됨
            - 이 때 가장 최고 등수보다 높아야 하므로 변수에 저장하여 갱신
    """
    import sys

    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        ranks = [list(map(int, input().split())) for _ in range(n)]
        ranks.sort()
        ans, prev_int = 0, 1e9

        for _, rank_int in ranks:
            if rank_int < prev_int:
                prev_int = rank_int
                ans += 1

        print(ans)


if __name__ == "__main__":
    try1()
