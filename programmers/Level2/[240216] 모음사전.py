"""
https://school.programmers.co.kr/learn/courses/30/lessons/84512
"""


def solution(word):
    """
    - 약 10분 풀이
    - 재귀로 글자를 계속 추가하되, 단어는 길이가 5를 넘어선 안됨 -> 백트래킹
        - 사실 주어진 사전의 길이가 작아 itertools 를 활용해도 되지만, 백트래킹으로 풀어보았음
    """
    seq = []
    ls = []

    def dfs(x):
        nonlocal ls
        if len(seq) > 5:
            return

        for i in "AEIOU":
            seq.append(i)
            if len(seq) <= 5:
                ls.append("".join(seq))
            dfs(i)
            seq.pop()

    dfs(0)
    return ls.index(word) + 1
