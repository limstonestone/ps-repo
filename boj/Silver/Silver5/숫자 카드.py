"""
https://www.acmicpc.net/problem/10815
"""


def try1():
    """
    - 약 2분 소요
    """
    import sys
    import bisect

    input = sys.stdin.readline
    n = int(input())
    own_cards = list(map(int, input().split()))
    own_cards.sort()

    m = int(input())
    cards_to_solve = list(map(int, input().split()))

    def bin_search(seq, num):
        idx = bisect.bisect_left(seq, num)
        return 1 if idx < n and seq[idx] == num else 0

    answer = []
    for card in cards_to_solve:
        answer.append(bin_search(own_cards, card))

    print(*answer)


if __name__ == "__main__":
    try1()
