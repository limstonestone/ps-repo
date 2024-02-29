"""
https://www.acmicpc.net/problem/1157
"""


def try1():
    """
    - 약 7분 소요
    - 입력길이가 최대 100만 -> O(N) ~ O(NlogN)
    - 딕셔너리의 키로 알파벳, 밸류로 카운트값을 주어 O(1)으로 접근
    """
    import sys
    from collections import defaultdict

    input = sys.stdin.readline
    strings = input().rstrip()
    answer = defaultdict(int)

    for x in strings:
        answer[x.upper()] += 1

    answer = sorted(
        answer.items(), key=lambda x: x[1], reverse=True
    )  # value 기준으로 정렬
    if len(answer) > 1:  # 인덱싱 오류 방지
        if (
            answer[0][1] == answer[1][1]
        ):  # 가장 많은 알파벳과 두번째로 많은 알파벳의 개수가 같다면 물음표 출력
            print("?")
            exit()

    print(answer[0][0])


if __name__ == "__main__":
    try1()
