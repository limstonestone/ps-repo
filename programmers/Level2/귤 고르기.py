"""
https://school.programmers.co.kr/learn/courses/30/lessons/138476
"""


def solution(k, tangerine):
    """
    - 약 10분 소요
    - 입력 길이 10만 -> O(N)
    - 종류가 가장 최소이려면, 가장 종류가 많은 것들을 우선으로 골라야함
        - 반대로 말하면 가장 종류가 적은 것들을 배제해야함
    - 가장 종류가 적은 것들 -> Counter 로 계산
    """
    from collections import Counter

    total_length = len(tangerine)
    arr = [(x, c) for x, c in Counter(tangerine).items()]  # pop 을 위해 리스트 변환
    arr.sort(key=lambda x: x[1], reverse=True)  # 고유값의 개수가 작은게 뒤로감

    i = 0  # i 는 배제시켜버린 귤의 개수, 따라서 최대는 total_length - k
    while True:
        key, val = arr.pop()  # 가장 종류가 적은 것 배제하기
        i += val  # 전체 개수에서 해당 종류의 개수만큼 뺌
        if (
            i > total_length - k
        ):  # 만약 필요한것 이상으로 빼버렸다면 다시 남은 개수를 넣어줘야함
            arr.append(0)  # 아까 뺐던거 넣은 것과 같은 처리(어차피 길이만 필요하므로)
            break

    return len(
        arr
    )  # 남아있는 종류들, 즉 가장 적은 종류들을 배제한 나머지 종류들의 길이
