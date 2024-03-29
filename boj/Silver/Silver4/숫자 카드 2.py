"""
https://www.acmicpc.net/problem/10816
"""


def try1():
    """
    - 0538
    - 주어진 수를 배열에서 탐색 -> 이분탐색
    - 이분탐색 시 해당 숫자를 찾으면 숫자가 달라질 때까지 idx 증가시키는 방식으로 구현
        -> 시간 초과
    - 애초에 수중의 카드의 개수를 미리 딕셔너리에 넣어놓고, 탐색 시 해당 숫자를 들고오도록 구현
    """
    import sys
    import bisect
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    own_cards = list(map(int, input().split()))
    own_cards.sort()
    key2val = Counter(own_cards)

    m = int(input())
    cards_to_solve = list(map(int, input().split()))

    def bin_search(seq, num):
        cnt = 0
        idx = bisect.bisect_left(seq, num)
        if idx < n and seq[idx] == num:
            cnt = key2val[num]
        return cnt

    answer = []
    for card in cards_to_solve:
        answer.append(bin_search(own_cards, card))

    print(*answer)


if __name__ == "__main__":
    try1()
