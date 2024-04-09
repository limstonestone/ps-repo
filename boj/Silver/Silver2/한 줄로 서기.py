"""
https://www.acmicpc.net/problem/1138
"""


def try1():
    """
    - 약 20분 소요
    - 일단 맨 마지막에 있는 친구의 값은 무조건 0 (어디 줄을 서든 자기보다 큰 키는 없음)
    - 입력 길이 최대 10으로 매우 짧음 -> 그냥 다 구한 다음 검증해도 문제 없을듯 함
        - 10 * 9 * 8 * 7 = 5040 -> 이중 반복문해도 문제 X
    """
    import sys
    from itertools import permutations as P

    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    for candidate in P(range(1, n + 1)):  # 가능한 모든 경우 고려
        answer_flag = True
        for height in candidate:
            cnt = 0
            i = 0  # 왼쪽부터 탐색
            while candidate[i] != height:
                if candidate[i] > height:
                    cnt += 1
                i += 1

            if cnt != arr[height - 1]:  # 카운트 했을 때 조건에 위배됬을 경우 종료
                answer_flag = False
                break

        if answer_flag:  # 위배된 규칙이 없을 경우
            print(*candidate)
            break


if __name__ == "__main__":
    try1()
