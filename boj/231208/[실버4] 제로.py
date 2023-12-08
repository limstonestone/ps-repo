"""
https://www.acmicpc.net/problem/10773
"""


def try1():
    """
    - 약 2분
    - 입력 K 가 10만 이하 -> O(NlogN)
    - 굳이 deqeue 을 활용하지 않고 스택(기본 list)으로도 풀이 가능
        - 스택이기 때문
    """

    import sys
    from collections import deque

    input = sys.stdin.readline

    K = int(input())
    moneys = deque()
    for _ in range(K):
        money = int(input())
        if money:
            moneys.append(money)
        else:
            moneys.pop()

    print(sum(moneys))


if __name__ == "__main__":
    try1()
