"""
https://www.acmicpc.net/problem/9375
"""


def try1():
    """
    - 약 1시간 풀이 후 실패로 답지 참조
    - 의상의 이름은 생각할 필요가 없음, 개수만 생각하면 됨 (중복해서 들어오지 않기 때문)

    - 답지 풀이
        - 답 = (a종류수 + 1) * (b종류수 + 1) * (c종류수 + 1) ... -1
        - +1 은 해당 종류를 안 입는 이유, -1 은 전부 다 안입는 경우
        - 문제 예시를, 즉 종류수를 카운팅하는 방법을 잘 못 이해한듯 함
    """
    import sys

    input = sys.stdin.readline

    total_n = int(input())

    for _ in range(total_n):
        n = int(input())
        clothes = dict()

        for _ in range(n):
            _, cloth_type = input().split()
            if not (cloth_type in clothes):
                clothes[cloth_type] = 0

            clothes[cloth_type] += 1

        cnt = 1

        for cloth_type in clothes.keys():  # 의상의 종류
            cnt *= clothes[cloth_type] + 1  # 해당 종류를 안 입는 경우도 포함

        print(cnt - 1)


if __name__ == "__main__":
    try1()
