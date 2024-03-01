"""
https://www.acmicpc.net/problem/10825
"""


def try1():
    """
    - 약 10분 풀이
    - 입력 범위가 10만 -> O(NlogN) ~ O(N) 으로 풀이
    - 리스트 내장 함수의 sort 를 사용하면 정렬 가능
        - 이 때, key 로 lambda 식을 작성하여 동시 기준의 정렬 가능
        - 증/감의 경우 마이너스를 활용할 수 있음
    """
    import sys

    input = sys.stdin.readline

    n = int(input())
    scores = []
    for _ in range(n):
        name, *score = input().split()
        score = [name] + [int(x) for x in score if x.isdigit()]
        scores.append(score)

    scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in range(n):
        print(scores[i][0])


if __name__ == "__main__":
    try1()
