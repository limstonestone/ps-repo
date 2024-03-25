"""
https://school.programmers.co.kr/learn/courses/30/lessons/258707
"""

from collections import deque


def solution(coin, cards):
    """
    - 약 1시간 20분 풀이 후 힌트 참조 -> +20분 풀이
    - 짝을 이루는 것을 확인하기위해 이분탐색을 활용할 수 있을듯 함
        - 라고 생각했지만 애초에 집합을 활용하는 게 존재 여부 확인 시 O(1)로 더 효율적

    - 버리는 것, 가지는 것의 차이가 뭘까?
        - 경우의 수를 따져보았는데 과거/현재/미래까지 다 생각해야함. 너무 복잡...

    - 힌트 참조
        - 매 라운드마다 실제 주어진 과정을 수행할 필요 없음
            - 그냥 뽑았던 카드를 기억하고 있다가 짝이 될 때 코인을 빼면 됨
                - 계속 패에 들고 있다가 내꺼에서 낼게 없으면 동전써서 대출하는 것과 같은 것
            - 즉 매 라운드 코인을 가장 적게 쓸 수 있는 방법을 고민하면 됨
        - 코인 0개 씀 -> 기존 카드에서 2개 냄
        - 코인 1개 씀 -> 기존 카드에서 1개, 현재 라운드까지 뽑은 카드 중 아직 가져오지 않은 거 1개
        - 코인 2개 씀 -> 현재 라운드까지 뽑은 카드 중 아직 가져오지 않은 거 2개
    """
    from collections import deque

    answer = 1
    n = len(cards)

    own_cards, remain_cards = set(cards[: n // 3]), deque(cards[n // 3 :])
    tmp_cards = set()  # 현재 라운드까지 뽑은 카드들

    while remain_cards:
        tmp_cards.add(remain_cards.popleft())
        tmp_cards.add(remain_cards.popleft())

        own_flag = False  # 내꺼에서 낼 게 있는지 여부

        for own_card in own_cards:
            if n + 1 - own_card in own_cards:
                own_flag = True
                break

        if own_flag:  # 내꺼에서 낼 게 있다면 내꺼 내기
            own_cards.discard(own_card)
            own_cards.discard(n + 1 - own_card)

        else:  # 낼게 없다면 기존 뽑아놓은 카드에서 대출 땡기기
            one_flag = False  # 동전 하나만 써도 가능한지 여부

            if coin >= 1:
                for tmp_card in set(tmp_cards):
                    if n + 1 - tmp_card in own_cards:
                        coin -= 1
                        own_cards.discard(n + 1 - tmp_card)  # 내꺼 하나
                        tmp_cards.discard(tmp_card)  # 뽑아놓은 거 하나
                        one_flag = True
                        break

            if not one_flag:  # 동전을 하나는 안되고 두개 써야 하는 경우
                two_flag = False
                if coin >= 2:
                    for tmp_card in set(tmp_cards):
                        if n + 1 - tmp_card in set(tmp_cards):
                            coin -= 2
                            tmp_cards.discard(tmp_card)
                            tmp_cards.discard(n + 1 - tmp_card)
                            two_flag = True
                            break

                else:  # 결국 2개까지써야 라운드를 넘어갈 수 있는데 코인이 없다면 종료
                    break

                if not two_flag:  # 뽑아놓은 카드들 중 2개가 짝이 안이루어져도 종료
                    break

        answer += 1

    return answer
