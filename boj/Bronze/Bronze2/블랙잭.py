"""
https://www.acmicpc.net/problem/2798
"""


def try1():
    """
    - 약 5분 소요
    - 3장을 고르는데 M을넘지않으면서 최대한 M에 가깝게
    - 카드의 개수 범위가 매우 작음(최대100) -> 일일히 구하는게 제일 빠를듯 함
        - 3중 반복문으로 해도 문제 없음
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    cards = list(map(int, input().split()))

    ans = 0
    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            for k in range(j + 1, len(cards)):
                temp_ans = cards[i] + cards[j] + cards[k]
                if temp_ans <= m:
                    ans = max(ans, temp_ans)

    print(ans)


if __name__ == "__main__":
    try1()
