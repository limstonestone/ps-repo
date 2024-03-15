"""
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""


def solution(sizes):
    """
    - 약 50분 풀이
    - 일단 w, h 중 가장 큰 쪽을 고정시키는 건 맞는 것 같음
    - 예시로 만약 가로가 가장 크다면, 세로 길이가 가로보다 큰 것들을 바꾸어야 할 것
        - 왜냐하면 회전하면 결과가 바뀔 수 있다는 뜻이기 때문
    - 이를 일반화 가능
        - 그냥 가로든 세로든 한쪽에 가장 큰 숫자들을 배열하면 됨
    """

    max_w = 0
    max_h = 0
    for w, h in sizes:
        if w < h:  # 가로에 더 큰수를 몰빵(세로에 몰빵해도 정답)
            w, h = h, w
        max_w = max(max_w, w)
        max_h = max(max_h, h)

    return max_w * max_h
