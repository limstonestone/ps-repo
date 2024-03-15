"""
https://www.acmicpc.net/problem/2805
"""


def try1():
    """
    - 약 30분 소요
    - 범위가 매우 크며 정해진 범위에서 값을 찾아야 함 -> 이진 탐색
    - 이진 탐색의 target 은 M 이 될 것
        - 탐색은 M을 기준으로 잘랐을 때 가져갈 수 있는 나무 길이
    - python3 대신 pypy로 제출했을 때 통과
    - answer 변수를 따로 지정하지 않고 end로만 정의해도 문제 없음
    """
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)

    start, end = 1, trees[0]
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        summation = 0
        for x in trees:
            if x - mid <= 0:
                break
            summation += x - mid

        if summation == m:
            answer = mid
            break

        elif summation < m:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    print(answer)


if __name__ == "__main__":
    try1()
